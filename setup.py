from setuptools import setup, find_packages

setup(
    name="signal-filter-visualizer",
    author="Juha-Matti Santero",
    author_email="juha.santero@gmail.com",
    description="Python tool for signal filter design with Qt interface.",
    license="GPL",
    version="dev",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "PyQt5",  # creates trouble with Anaconda because its package is named as pyqt
        "numpy",
        "scipy",
        "matplotlib",
        "kblom==dev",
    ],
    dependency_links=[
        "https://github.com/kblomqvist/kblom.py/tarball/master#egg=kblom-dev",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    url="https://github.com/jsantero/signal-filter-visualizer",
)
