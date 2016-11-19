# Description

Signal Filter Visualizer is a Python program meant as a tool for
signal processing filter design. To this end it uses signal processing
functionality provided by Scipy and Numpy. Matplotlib is used to plot the
signals. GUI is also a very essential part of the program, since without it,
the user would be better off just writing his own signal processing script.
GUI is built with PyQt5, because it is powerful, versatile and very easy to use.

Signal Filter Visualizer features:
* Signal generation
* Import signal from file
* Noise generation
* Filtering
 * Butterworth
 * Chebyshev I & II
 * Bessel
 * Elliptic
 * Rolling window median, RMS and mean
* Visualization of filtered and unfiltered signals

# Installation instructions

Clone the repository.
> git clone https://github.com/jsantero/signal-filter-visualizer.git

Install the required packages with pip.
> pip install PACKAGENAME

If you're unfamiliar with pip please see
https://packaging.python.org/installing/

Using a virtual environment is recommended. Please see
https://docs.python.org/3/library/venv.html

## Requirements:
* Python3 (tested on version 3.5.2)
* PyQt5 (tested on version 5.7)
* numpy (tested on version 1.11.2+mkl)
* scipy (tested on version 0.18.1)
* matplotlib (tested on version 1.5.3)
* kblom (from github)
 * To install: pip install git+https://github.com/kblomqvist/kblom.py.git

## Running the program
> python signal_filter_visualizer.py

## Common problems
*I have problems installing a package with pip*

Sometimes pip cannot find the correct package that you want. Instead of
downloading the package through pip, you can usually find a wheel file (.whl)
from a non-standard host, and install it from the file with pip. For example,
website listing Python packages is located at
http://www.lfd.uci.edu/~gohlke/pythonlibs/. Use it at your own risk.

*I cannot get the program running on Linux*

This project has been so far developed in Windows, and Linux compatibility is
not guaranteed. All of the project's components should function well under Linux
but installation process may be more complicated.

# Where to get help

## Installing PyQt5
http://pyqt.sourceforge.net/Docs/PyQt5/installation.html

## PyQt5 reference
http://pyqt.sourceforge.net/Docs/PyQt5/

## Scipy signal processing reference
https://docs.scipy.org/doc/scipy-0.18.1/reference/signal.html

# Credits and Inspiration

The initial idea for this project is from Kim Blomqvist. See his github at
https://github.com/kblomqvist
