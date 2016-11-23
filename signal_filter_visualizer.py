import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from widgets import MainWidget
from dialogs import SignalLoaderDlg
from classes import signalchain as chain

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        #_mainWidget = MainWidget(self)
        #self.setCentralWidget(_mainWidget)
        self.setWindowTitle("Signal Filter Visualizer")

        fileOpenAction = QAction(QIcon("icons/open.png"), "&Open", self)
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

        fileToolbar = self.addToolBar("File")
        fileToolbar.setObjectName("FileToolBar")
        fileToolbar.addAction(fileOpenAction)

        # Contains elements of a signal chain where one element's output is
        # routed to the following element's input
        self.container = chain.ChainContainer()

        # Dock widget for presenting contents of signal chain container
        containerDockWidget = QDockWidget("Signal Chain", self)

    def openFile(self):
        dlg = SignalLoaderDlg()
        if dlg.exec_():
            data = dlg.data
            self.container.add(data)
            print(dlg.data)

    def quit(self):
        self.close()

def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()


main()
