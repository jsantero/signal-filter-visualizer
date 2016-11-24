from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from kblom.dsp import timeseries as ts

class Rolling(QWidget):

    filterTypes = {'Mean': 'mean', 'Root-Mean-Square':'rms',
                   'Median': 'median'}
    valuesChanged = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__()

        typeLabel = QLabel("Type")
        samplingRateLabel = QLabel("Sampling Rate")
        windowLengthLabel = QLabel("Window Length")

        self.typeComboBox = QComboBox()
        self.typeComboBox.addItems(self.filterTypes.keys())
        self.samplingRateBox = QSpinBox()
        self.samplingRateBox.setRange(0, 100000)
        self.samplingRateBox.setValue(100)
        self.samplingRateBox.setSuffix(" Hz")
        self.windowLengthBox = QSpinBox()
        self.windowLengthBox.setRange(1, 10000000)
        self.windowLengthBox.setValue(10)

        self.typeComboBox.currentIndexChanged.connect(self.updateUi)
        self.samplingRateBox.valueChanged.connect(self.updateUi)
        self.windowLengthBox.valueChanged.connect(self.updateUi)

        grid = QGridLayout()
        grid.addWidget(typeLabel, 0, 0)
        grid.addWidget(samplingRateLabel, 1, 0)
        grid.addWidget(windowLengthLabel, 2, 0)
        grid.addWidget(self.typeComboBox, 0, 1)
        grid.addWidget(self.samplingRateBox, 1, 1)
        grid.addWidget(self.windowLengthBox, 2, 1)
        self.setLayout(grid)

        self.updateUi()

    def updateUi(self):
        self.valuesChanged.emit()

    def returnFunction(self):
        self._type = self.filterTypes[self.typeComboBox.currentText()]
        self.samplingRate = self.samplingRateBox.value()
        self.windowLength = self.windowLengthBox.value()
        return self.filter

    def filter(self, data):
        if not data or data[0] is 0 or data[1] is 0:
            return None
        x, y = data
        if self.samplingRate is 0:
            self.samplingRate = None

        if self._type == 'mean':
            sma = ts.RollingMean(self.windowLength, self.samplingRate)
            signal = list(sma.roll(y, end=True))
        elif self._type == 'rms':
            rms = ts.RollingRootMeanSquare(self.windowLength, self.samplingRate)
            signal = list(rms.roll(y, end=True))
        elif self._type == 'median':
            m = ts.RollingMedian(self.windowLength, self.samplingRate)
            signal = list(m.roll(y, end=True))
        data = (x, signal)
        return data
