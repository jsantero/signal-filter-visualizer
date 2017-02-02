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

class FilterDlg(QDialog):

    def __init__(self, parent=None):
        super().__init__()

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
        buttonBox.accepted.connect(self.acceptFilter)
        buttonBox.rejected.connect(self.reject)

        grid = QGridLayout()
        grid.addWidget(filterLabel, 0, 0, 1, 1)
        grid.addWidget(self.filterComboBox, 0, 1, 1, 1)
        grid.addWidget(self.stackedWidget, 1, 0, 1, 2)
        grid.addWidget(buttonBox, 2, 0, 1, 2)
        self.setLayout(grid)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)

    def updateUi(self):
        pass

    def changeFilter(self):
        selectedFilter = self.filterDispatcher[
            self.filterComboBox.currentText()]
        self.stackedWidget.setCurrentWidget(selectedFilter)

    def acceptFilter(self):
        currentlySelected = self.stackedWidget.currentWidget()
        function = currentlySelected.returnFunction()

        self.newElement = ChainElement(name="Filter")
        self.newElement.function = function
        self.newElement.update()
        self.accept()
