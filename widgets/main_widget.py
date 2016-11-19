from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from .signal_loader_widget import SignalLoaderWidget
from .signal_generator_widget import SignalGenerator
from .noise_generator_widget import NoiseGenerator
from .filter_widget import Filter


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)

    def plot(self, data):
        self.figure.clear()
        if isinstance(data, tuple) and data[1] is not 0:
            ax = self.figure.add_subplot(111)
            try:
                ax.plot(*data, 'r-')
            except ValueError as e:
                print("Error while plotting: {}".format(e))
        self.draw()


class MainWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.loader = SignalLoaderWidget()
        self.generator = SignalGenerator()
        self.noise = NoiseGenerator()
        self.filter = Filter()

        self.tabWidget = QTabWidget()
        self.tabWidget.addTab(self.loader, "Load file")
        self.tabWidget.addTab(self.generator, "Signal generator")

        self.canvasRaw = PlotCanvas(self)
        self.toolbarRaw = NavigationToolbar(self.canvasRaw, self)
        self.canvasFiltered = PlotCanvas(self)
        self.toolbarFiltered = NavigationToolbar(self.canvasFiltered, self)

        layout = QGridLayout()
        layout.addWidget(self.tabWidget, 0, 0, 1, 3)
        layout.addWidget(self.noise, 0, 1, 1, 1)
        layout.addWidget(self.filter, 0, 2, 1, 1)
        layout.addWidget(self.canvasRaw, 1, 0)
        layout.addWidget(self.toolbarRaw, 2, 0)
        layout.addWidget(self.canvasFiltered, 1, 1)
        layout.addWidget(self.toolbarFiltered, 2, 1)
        self.setLayout(layout)

        self.loader.signalReady.connect(self.noise.addNoise)
        self.generator.generatorChanged.connect(self.noise.addNoise)
        self.noise.noiseAdded.connect(self.filter.applyFilter)
        self.noise.noiseAdded.connect(self.canvasRaw.plot)
        self.filter.signalFiltered.connect(self.canvasFiltered.plot)
