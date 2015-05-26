# colorcif.py

A small utility python script to generate high-quality images from cif files
with symmetry unique atoms colored with different colors

## Installation

## Usage

* color all symmetry unique atoms

  ```{r, engine='bash'}
  colorcif.py TON.cif -o ton_default.pov
  ```

  ![TON default test][ton_default]



[ton_default]: https://bytebucket.org/lukaszmentel/colorcif/raw/tip/example/gfx/ton_default.png "TON default"



## Dependencies


* [ase](https://wiki.fysik.dtu.dk/ase/)
* [numpy](http://www.numpy.org/)
* [matplotlib](http://matplotlib.org/)


## Additional info

[ase example](https://wiki.fysik.dtu.dk/ase/_downloads/saving_graphics.py)
