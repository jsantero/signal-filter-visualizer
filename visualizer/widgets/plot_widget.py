from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

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

class PlotWidget(QWidget):
    def __init__(self, data):
        super().__init__()
        self.canvas = PlotCanvas()
        self.toolbar = NavigationToolbar(self.canvas, self)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.toolbar)
        self.setLayout(layout)

        self.canvas.plot(data)

    def redraw(self, data):
        self.canvas.plot(data)
