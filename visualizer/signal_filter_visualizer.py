import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#from widgets.main_widget import MainWidget
from visualizer.widgets.container_list_widget import ContainerListWidget
from visualizer.dialogs.file_open_dlg import SignalLoaderDlg
from visualizer.dialogs.filter_widget_dlg import FilterDlg
from visualizer.classes import signalchain as chain
from visualizer.widgets.plot_widget import PlotWidget

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Signal Filter Visualizer")

        fileMenu = self.menuBar().addMenu("&File")
        createMenu = self.menuBar().addMenu("&Create")
        graphMenu = self.menuBar().addMenu("Graph")
        fileToolBar = self.addToolBar("File")
        fileToolBar.setObjectName("FileToolBar")
        createToolBar = self.addToolBar("Create")
        createToolBar.setObjectName("CreateToolBar")
        graphToolBar = self.addToolBar("Graph")
        graphToolBar.setObjectName("GraphToolBar")

        self.addAction(
            "&Open", self.openFile, fileMenu, icon="icons/open.png",
            helpText="Import samples from a file", toolBar=fileToolBar,
            shortCut=QKeySequence.Open)
        self.addAction("&Quit", self.quit, fileMenu, shortCut=QKeySequence.Quit)
        self.addAction(
            "Draw", self.drawGraph, graphMenu, icon="icons/graph.png",
            helpText="Draw graph based on currently selected source",
            toolBar=graphToolBar)
        self.addAction(
            "New Filter", self.addFilter, createMenu, icon="icons/filter.png",
            helpText="Create new filter as part of signal chain",
            toolBar=createToolBar)

        self.centralWidget = ContainerListWidget(chain.ChainContainer())
        self.setCentralWidget(self.centralWidget)

        self.graphList = []

    def addAction(self, name, slot, fileMenu, icon=None,
                  helpText=None, toolBar=None, shortCut=None):
        if icon:
            action = QAction(QIcon(icon), name, self)
        else:
            action = QAction(name, self)
        if shortCut:
            action.setShortcut(shortCut)
        if helpText:
            action.setToolTip(helpText)
            action.setStatusTip(helpText)
        action.triggered.connect(slot)
        fileMenu.addAction(action)
        if toolBar:
            toolBar.addAction(action)

    def openFile(self):
        dlg = SignalLoaderDlg()
        if dlg.exec_():
            element = dlg.newElement
            self.centralWidget.add(element)

    def addFilter(self):
        dlg = FilterDlg()
        if dlg.exec_():
            element = dlg.newElement
            self.centralWidget.add(element)

    def drawGraph(self):
        selectedRow = self.centralWidget.listWidget.currentRow()
        selectedElement = self.centralWidget.container.chainList[selectedRow]
        data = selectedElement.output
        name = selectedElement.name
        numberOfGraphs = len(self.graphList)
        plotDockWidget = QDockWidget(name, self)
        plotDockWidget.setObjectName("GraphDockWidget{}".format(numberOfGraphs))
        plotDockWidget.setAllowedAreas(Qt.LeftDockWidgetArea|
                                       Qt.RightDockWidgetArea)
        plotDockWidget.setWidget(PlotWidget(data))
        self.addDockWidget(Qt.RightDockWidgetArea, plotDockWidget)
        self.graphList.append(plotDockWidget)

    def quit(self):
        self.close()

def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()


main()
