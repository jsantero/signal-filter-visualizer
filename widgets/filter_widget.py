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


class Filter(QWidget):

    signalFiltered = pyqtSignal(tuple)

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
        filters = sorted(self.filterDispatcher.keys())
        self.filterComboBox.addItems(filters)

        filterLabel.setBuddy(self.filterComboBox)

        self.filterComboBox.currentIndexChanged.connect(self.changeFilter)
        butter.valuesChanged.connect(self.updateUi)
        bessel.valuesChanged.connect(self.updateUi)
        cheby1.valuesChanged.connect(self.updateUi)
        cheby2.valuesChanged.connect(self.updateUi)
        elliptic.valuesChanged.connect(self.updateUi)
        rolling.valuesChanged.connect(self.updateUi)

        grid = QGridLayout()
        grid.addWidget(filterLabel, 0, 0, 1, 1)
        grid.addWidget(self.filterComboBox, 0, 1, 1, 1)
        grid.addWidget(self.stackedWidget, 1, 0, 1, 2)
        self.setLayout(grid)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)

        self.latestData = None

    def changeFilter(self):
        selectedFilter = self.filterDispatcher[
            self.filterComboBox.currentText()]
        self.stackedWidget.setCurrentWidget(selectedFilter)
        self.updateUi()

    def updateUi(self):
        if self.latestData:
            self.applyFilter(self.latestData)

    def applyFilter(self, data):
        if data and data[0] is not 0 and data[1] is not 0:
            self.latestData = data
            currentlySelected = self.stackedWidget.currentWidget()
            # Each filter has separately defined filter-method
            data = currentlySelected.filter(self.latestData)
        else: data = (0,0)
        self.signalFiltered.emit(data)
