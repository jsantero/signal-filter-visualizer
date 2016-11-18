from setuptools import setup, find_packages

setup(
    name="signal-filter-visualizer",
    author="Juha-Matti Santero",
    author_email="juha.santero@gmail.com",
    description="Python tool for signal filter design with Qt interface.",
    license="GPL",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "PyQt5",
        "numpy",
        "scipy",
        "matplotlib",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    url="https://github.com/jsantero/signal-filter-visualizer",
)
