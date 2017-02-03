import numpy as np
import scipy.signal

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from .filter_variants import Bessel
from .filter_variants import Butter
from .filter_variants import Cheby1
from .filter_variants import Cheby2
from .filter_variants import Elliptic
from .filter_variants import Rolling
from visualizer.classes.signalchain import ChainElement
from visualizer.widgets.plot_widget import PlotWidget

class FilterDlg(QDialog):

    def __init__(self, centralWidget, parent=None):
        super().__init__()
        self.setWindowTitle("Add filter")

        self.filterDispatcher = {
            'Bessel/Thomson': Bessel(),
            'Butterworth': Butter(),
            'Chebyshev type I': Cheby1(),
            'Chebyshev type II': Cheby2(),
            'Elliptic (Cauer)': Elliptic(),
            'Rolling window': Rolling()
        }

        filterLabel = QLabel("Filter")
        self.filterComboBox = QComboBox()
        filterLabel.setBuddy(self.filterComboBox)
        # Stacked widget stores simultaneously all different filters but shows
        # only the one currently selected
        self.stackedWidget = QStackedWidget()
        checkBoxLabel = QLabel("Preview")
        self.checkBox = QCheckBox()  # For toggling signal preview
        checkBoxLabel.setBuddy(self.checkBox)
        self.checkBox.setTristate(False)
        self.checkBox.setChecked(False)
        self.checkBox.stateChanged.connect(self.updateUi)

        for key, value in self.filterDispatcher.items():
            self.stackedWidget.addWidget(value)
            value.valuesChanged.connect(self.updateUi)

        # Add filter names in the combobox in alphabetical order
        filters = sorted(self.filterDispatcher.keys())
        self.filterComboBox.addItems(filters)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok|
                                     QDialogButtonBox.Cancel)
        buttonBox.button(QDialogButtonBox.Ok).setDefault(True)

        self.filterComboBox.currentIndexChanged.connect(self.changeFilter)
        self.checkBox.stateChanged.connect(self.updateUi)
        buttonBox.accepted.connect(self.acceptFilter)
        buttonBox.rejected.connect(self.rejectFilter)

        grid = QGridLayout()
        grid.addWidget(filterLabel, 0, 0, 1, 1)
        grid.addWidget(self.filterComboBox, 0, 1, 1, 1)
        grid.addWidget(self.stackedWidget, 1, 0, 1, 2)
        grid.addWidget(checkBoxLabel, 2, 0, 1, 1)
        grid.addWidget(self.checkBox, 2, 1, 1, 1)
        grid.addWidget(buttonBox, 3, 0, 1, 2)
        self.setLayout(grid)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)

        self.previewPlot = None
        self.previewDlg = None  # Reference to prevent garbage collection
        self.centralWidget = centralWidget

    # When filter settings are changed
    def updateUi(self):
        if self.checkBox.checkState():  # Draw preview of filtered signal
            currentlySelected = self.stackedWidget.currentWidget()
            function = currentlySelected.returnFunction()
            data = self.centralWidget.getData()

            previewElement = ChainElement(name="Preview")
            previewElement.function = function
            previewElement.input_ = data
            previewElement.update()
            data = previewElement.output
            if self.previewPlot:  # PlotWidget created already
                self.previewPlot.redraw(data)
            else:  # PlotWidget not yet created
                self.previewPlot = PlotWidget(data)
                self.previewDlg = QDialog()
                self.previewDlg.setWindowTitle("Signal Preview")
                grid = QGridLayout()
                grid.addWidget(self.previewPlot)
                self.previewDlg.setLayout(grid)
                self.previewDlg.show()

    def changeFilter(self):
        selectedFilter = self.filterDispatcher[
            self.filterComboBox.currentText()]
        self.stackedWidget.setCurrentWidget(selectedFilter)

    def rejectFilter(self):
        if self.previewDlg:
            self.previewDlg.reject()
        self.reject()

    def acceptFilter(self):
        currentlySelected = self.stackedWidget.currentWidget()
        function = currentlySelected.returnFunction()

        newElement = ChainElement(name="Filter")
        newElement.function = function
        newElement.update()
        self.centralWidget.add(newElement)  # Add to container list widget
        if self.previewDlg:
            self.previewDlg.accept()

        self.accept()
