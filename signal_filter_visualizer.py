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

        fileOpenAction = QAction("&Open", self)
        fileOpenAction.setShortcut(QKeySequence.Open)
        helpText = "Import samples from a file"
        fileOpenAction.setToolTip(helpText)
        fileOpenAction.setStatusTip(helpText)
        fileOpenAction.triggered.connect(self.openFile)

        fileQuitAction = QAction("&Quit", self)
        fileQuitAction.setShortcut(QKeySequence.Quit)
        fileQuitAction.triggered.connect(self.quit)

        fileMenu = self.menuBar().addMenu("&File")
        fileMenu.addAction(fileOpenAction)
        fileMenu.addAction(fileQuitAction)

    def openFile(self):
        print("foo")

    def quit(self):
        self.close()

def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()


main()
