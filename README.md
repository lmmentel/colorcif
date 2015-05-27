# colorcif.py

A small utility python script to generate high-quality images from cif files
with symmetry unique atoms colored with different colors


## Dependencies

First make sure you have the following dependencies installed:

* [ase](https://wiki.fysik.dtu.dk/ase/)
* [numpy](http://www.numpy.org/)
* [matplotlib]

## Installation

After downloading and unpacking or cloning the repository run the standard
`setuptools` command

```
python setup.py install [--user]
```

## Usage

The scipt takes the following optional arguments that can be display with the
standard **-h** flag:

```
colorcif.py -h
```

### Examples

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
colorcif.py -O -c gist_rainbow -o ton_gist_rainbow_O.pov -x 30 -y 30 -z 30 TON.cif
```

  ![TON image][ton_gist_rainbow_O]

* color only oxygen atoms using `gist_rainbow` colormap from [matplotlib] and
rotate the unit cell 30 degrees with respect to each (x, y, z) axes and the
`glass` texture

  ```
  colorcif.py -O -c gist_rainbow -o ton_gist_rainbow_O.pov -x 30 -y 30 -z 30 -t glass TON.cif
  ```

  ![TON image][ton_gist_rainbow_glass_O]

[ton_default]: https://bytebucket.org/lukaszmentel/colorcif/raw/tip/example/gfx/ton_default.png "TON default all atoms"
[ton_RdYlGn_T]: https://bytebucket.org/lukaszmentel/colorcif/raw/tip/example/gfx/ton_RdYlGn_T.png "TON RdYlGn T-atoms"
[ton_RdYlBu_O]: https://bytebucket.org/lukaszmentel/colorcif/raw/tip/example/gfx/ton_RdYlBu_O.png "TON RdYlbu O-atoms"
[ton_gist_rainbow_O]: https://bytebucket.org/lukaszmentel/colorcif/raw/tip/example/gfx/ton_gist_rainbow_O.png "TON gist_rainbow O-atoms"
[ton_gist_rainbow_glass_O]: https://bytebucket.org/lukaszmentel/colorcif/raw/tip/example/gfx/ton_gist_rainbow_glass_O.png "TON gist_rainbow glass O-atoms"


[matplotlib]: http://matplotlib.org/


## Additional info

The script is based on the example from the [ase documentation](https://wiki.fysik.dtu.dk/ase/_downloads/saving_graphics.py).

## License

The MIT License (MIT)  

Copyright (c) 2015 Lukasz Mentel  

Permission is hereby granted, free of charge, to any person obtaining a copy  
of this software and associated documentation files (the "Software"), to deal  
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:  

The above copyright notice and this permission notice shall be included in all   
copies or substantial portions of the Software.  

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
SOFTWARE.  
