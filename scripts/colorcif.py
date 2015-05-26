'''
A small CLI script to genereate high-quality images from cif files with symmetry
non-unique atoms colored with different colors.
'''

import argparse
import os
import numpy as np
from pylab import get_cmap, cm

import ase.io
from ase.data.colors import jmol_colors

WHITE = (1.000, 1.000, 1.000)
LGRAY = (0.800, 0.800, 0.800)

def hsv2rgb(h, s, v):
    """http://en.wikipedia.org/wiki/HSL_and_HSV

    h (hue) in [0, 360[
    s (saturation) in [0, 1]
    v (value) in [0, 1]

    return rgb in range [0, 1]
    """
    if v == 0:
        return 0, 0, 0
    if s == 0:
        return v, v, v

    i, f = divmod(h / 60., 1)
    p = v * (1 - s)
    q = v * (1 - s * f)
    t = v * (1 - s * (1 - f))

    if i == 0:
        return v, t, p
    elif i == 1:
        return q, v, p
    elif i == 2:
        return p, v, t
    elif i == 3:
        return p, q, v
    elif i == 4:
        return t, p, v
    elif i == 5:
        return v, p, q
    else:
        raise RuntimeError('h must be in [0, 360]')

def hsv(array, s=.9, v=.9):

    array = (array - array.min()) * 359. / (array.max() - array.min())
    result = np.empty((len(array.flat), 3))
    for rgb, h in zip(result, array.flat):
        rgb[:] = hsv2rgb(h, s, v)
    return np.reshape(result, array.shape + (3,))

def get_colors(cmap, array):
    '''
    Get `numc` from a matplotlib colormap `cmap`
    '''

    cm = get_cmap(cmap)
    grid = (array - array.min())*1.0/(array.max() - array.min())
    result = np.zeros((len(array), 3))
    for rgb, x in zip(result, grid):
        rgb[:] = cm(x)[:3]
    return result


def main():

    colormaps = [m for m in cm.datad.keys() if not m.endswith("_r")]
    parser = argparse.ArgumentParser()
    parser.add_argument("cif", help="cif file")
    parser.add_argument("-t", "--texture",
                        choices=['jmol', 'glass', 'ase3', 'vmd'],
                        default="jmol")
    parser.add_argument("-T",
                        action="store_true",
                        help="highlight only different T-atoms")
    parser.add_argument("-O",
                        action="store_true",
                        help="highlight only atoms that are NOT T-atoms")
    parser.add_argument("-c", "--colormap",
                        choices=colormaps,
                        default=None, help="matplotlib colormap see: http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps")
    parser.add_argument("-o", "--output",
                        help="name of the output file",
                        default=None)
    args = parser.parse_args()

    if args.output is None:
        args.output = os.path.splitext(args.cif)[0] + '.pov'

    mol = ase.io.read(args.cif)

    sg = mol.info['spacegroup']

    mol.set_tags(sg.tag_sites(mol.get_scaled_positions()))

    rotation = '0x, 0y, 0z' # found using ase-gui menu 'view -> rotate'

    natoms = np.shape(mol.get_positions())[0]

    # set which atoms to color and how
    colors = np.zeros((natoms, 3))
    if not (args.T or args.O):
        if args.colormap:
            colors = get_colors(args.colormap, mol.get_tags())
        else:
            colors = hsv(mol.get_tags())
    else:
        # create a mask to select the T atoms and the rest
        Tmask = mol.get_atomic_numbers() != 8
        notTmask = np.logical_not(Tmask)
        if args.T:
            tags = mol.get_tags()[Tmask]
            if args.colormap:
                colors[Tmask] = get_colors(args.colormap, tags)
            else:
                colors[Tmask] = hsv(tags)
            # set the color of other atoms to gray
            colors[notTmask] = np.tile(np.asarray(LGRAY), (notTmask.sum(), 1))
            # default ase atom colors from jmol
            #colors[notTmask] = jmol_colors[mol.get_atomic_numbers()[notTmask]]
        elif args.O:
            tags = mol.get_tags()[notTmask]
            if args.colormap:
                colors[notTmask] = get_colors(args.colormap, tags)
            else:
                colors[notTmask] = hsv(tags)
            # set the color of other atoms to gray
            colors[Tmask] = np.tile(np.asarray(LGRAY), (Tmask.sum(), 1))
            # default ase atom colors from jmol
            #colors[Tmask] = jmol_colors[mol.get_atomic_numbers()[Tmask]]

    # Textures
    tex = [args.texture,] * natoms

    # keyword options for eps, pngand pov files
    kwargs = {
    'rotation': rotation,
    'show_unit_cell': 0,
    'colors': colors,
    'radii': None,
    }

    # keyword options for povray files only
    extra_kwargs = {
    'display'      : False, # Display while rendering
    'pause'        : False, # Pause when done rendering (only if display)
    'transparent'  : False, # Transparent background
    'canvas_width' : 400,  # Width of canvas in pixels
    'canvas_height': None,  # Height of canvas in pixels
    'camera_dist'  : 50.,   # Distance from camera to front atom
    'image_plane'  : None,  # Distance from front atom to image plane
                            # (focal depth for perspective)
    'camera_type'  : 'perspective', # perspective, ultra_wide_angle
    'point_lights' : [],             # [[loc1, color1], [loc2, color2],...]
    'area_light'   : [(2., 3., 40.) ,# location
                    'White',       # color
                    .7, .7, 3, 3], # width, height, Nlamps_x, Nlamps_y
    'background'   : 'White',        # color
    'textures'     : tex, # Length of atoms list of texture names
    'celllinewidth': 0.05, # Radius of the cylinders representing the cell
    }

    # Make the color of the glass beads semi-transparent
    #colors2 = np.zeros((natoms, 4))
    #colors2[:, :3] = colors
    #colors2[:, 3] = 0.95
    kwargs['colors'] = colors
    kwargs.update(extra_kwargs)

    # Make the raytraced image
    ase.io.write(args.output, mol, run_povray=True, **kwargs)

if __name__ == "__main__":
    main()
