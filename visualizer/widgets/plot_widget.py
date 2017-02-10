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
        """Plot one or multiple graphs in a figure.

        Plot data in either (x,y) form, or give a third data array to be
        drawn in a subplot. The output signal of a filter can then be visually
        compared to its input signal.
        Arguments:
        data -- (tuple) where 1st element is x, 2nd element is output of signal
                        chain element (e.g. filter) and optional 3rd element
                        is the input of element
        """
        self.figure.clear()
        try:
            if isinstance(data, tuple) and data[1] is not 0:
                if len(data) == 2:
                    ax1 = self.figure.add_subplot(111)
                if len(data) == 3:
                    ax1 = self.figure.add_subplot(211)
                ax1.plot(data[0], data[1], 'r-', label="Output")
            if len(data) == 3 and data[2] is not 0:
                ax2 = self.figure.add_subplot(212)
                ax2.plot(data[0], data[2], 'b-', label="Input")
                ax1.legend(loc='upper left')
                ax2.legend(loc='upper left')
            self.draw()
        except ValueError as e:
            print("Error while plotting: {}".format(e))

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
