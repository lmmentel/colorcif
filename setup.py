
''' colorcif script '''

from setuptools import setup

def readme():
    '''Return the contents of the README.md file.'''
    with open('README.md') as freadme:
        return freadme.read()


setup(
    author = "Lukasz Mentel",
    author_email = "lmmentel@gmail.com",
    scripts=[
        'scripts/colorcif.py',],
    description = "Script for coloring symmetry unique atoms",
    install_requires = [
        'matplotlib',
        'python-ase',
        'numpy',
    ],
    license = open('LICENSE.txt').read(),
    long_description = readme(),
    name = 'colorcif.py',
    url = 'https://bitbucket.org/lukaszmentel/colorcif/',
    version = '0.1.0',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
    ],
)
