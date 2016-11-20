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

1. Install Anaconda 4.2.0 for Windows (Python 3.5 version), https://www.continuum.io/downloads

2. Open Command Prompt and create new conda environment: conda create -n signals python=3.5 pyqt=5.6 numpy scipy matplotlib

3. Activate the new environment as instructed by conda: activate signals

4. Change your current working directory to your workspace and git clone signal-filter-visualizer: git clone https://github.com/jsantero/signal-filter-visualizer.git

5. Install signal-filter-visualizer (editable): pip install --process-dependency-links -e signal-filter-visualizer

# Running the program
> python signal_filter_visualizer.py

# Common problems

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
