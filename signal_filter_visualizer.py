import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from widgets import MainWidget


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        _mainWidget = MainWidget(self)
        self.setCentralWidget(_mainWidget)
        self.setWindowTitle("Signal Filter Visualizer")


def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()


main()
