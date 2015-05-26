# colorcif.py

A small utility python script to generate high-quality images from cif files
with symmetry unique atoms colored with different colors

## Installation

## Usage

* color all symmetry unique atoms

  ```
  colorcif.py TON.cif -o ton_default.pov
  ```

  ![TON image][ton_default]

* color only T-atoms using `RdYlGn` colormap from [matplotlib]

  ```
  colorcif.py -T -c RdYlGn -o ton_RdYlGn_T.pov TON.cif
  ```

  ![TON image][ton_RdYlGn_T]

* color only oxygen atoms using `RdYlBu` colormap from [matplotlib]

  ```
  colorcif.py -O -c RdYlBu -o ton_RdYlBu_O.pov TON.cif
  ```

  ![TON image][ton_RdYlBu_O]

* color only oxygen atoms using `gist_rainbow` colormap from [matplotlib] and
rotate the unit cell 30 degrees with respect to each (x, y, z) axes

  ```
  colorcif.py -O -c RdYlBu -o ton_RdYlBu_O.pov -x 30 -y 30 -z 30 TON.cif
  ```

  ![TON image][ton_gist_rainbow_O]

[ton_default]: https://bytebucket.org/lukaszmentel/colorcif/raw/tip/example/gfx/ton_default.png "TON default all atoms"
[ton_RdYlRn_T]: https://bytebucket.org/lukaszmentel/colorcif/raw/tip/example/gfx/ton_RdYlGn_T.png "TON RdYlGn T-atoms"
[ton_RdYlBu_O]: https://bytebucket.org/lukaszmentel/colorcif/raw/tip/example/gfx/ton_RdYlBu_O.png "TON RdYlbu O-atoms"
[ton_gist_rainbow_O]: https://bytebucket.org/lukaszmentel/colorcif/raw/tip/example/gfx/ton_gist_rainbow_O.png "TON gist_rainbow O-atoms"

## Dependencies


* [ase](https://wiki.fysik.dtu.dk/ase/)
* [numpy](http://www.numpy.org/)
* [matplotlib]

[matplotlib]: http://matplotlib.org/


## Additional info

[ase example](https://wiki.fysik.dtu.dk/ase/_downloads/saving_graphics.py)
