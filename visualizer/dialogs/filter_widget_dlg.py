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

        # Stacked widget stores simultaneously all different filters but shows
        # only the one currently selected
        self.stackedWidget = QStackedWidget()
        bessel = Bessel()
        butter = Butter()
        cheby1 = Cheby1()
        cheby2 = Cheby2()
        elliptic = Elliptic()
        rolling = Rolling()
        self.stackedWidget.addWidget(bessel)
        self.stackedWidget.addWidget(butter)
        self.stackedWidget.addWidget(cheby1)
        self.stackedWidget.addWidget(cheby2)
        self.stackedWidget.addWidget(elliptic)
        self.stackedWidget.addWidget(rolling)

        # Pairs the filter widget to a string so stackedWidget can be updated
        self.filterDispatcher = {
            'Bessel/Thomson': bessel,
            'Butterworth': butter,
            'Chebyshev type I': cheby1,
            'Chebyshev type II': cheby2,
            'Elliptic (Cauer)': elliptic,
            'Rolling window': rolling
        }

        filterLabel = QLabel("Filter")
        self.filterComboBox = QComboBox()
        filterLabel.setBuddy(self.filterComboBox)
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
