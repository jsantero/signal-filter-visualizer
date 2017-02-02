from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import numpy as np

from kblom.dsp import timeseries as ts

class Rolling(QWidget):

    filterTypes = {'Mean': 'mean', 'Root-Mean-Square':'rms',
                   'Median': 'median', 'Max':'max'}
    valuesChanged = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__()

        instructionLabel = QLabel(
            "If sampling rate is set as 0, set window length as number of "
            "samples.\nIf window length is even number, it will be incremented "
            "by one.\nIf sampling rate is set, specify length as seconds."
        )
        typeLabel = QLabel("Type")
        samplingRateLabel = QLabel("Sampling Rate")
        windowLengthLabel = QLabel("Window Length")

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)

        self.typeComboBox = QComboBox()
        self.typeComboBox.addItems(self.filterTypes.keys())
        self.samplingRateBox = QSpinBox()
        self.samplingRateBox.setRange(0, 100000)
        self.samplingRateBox.setValue(0)
        self.oldSampleRate = self.samplingRateBox.value()
        self.samplingRateBox.setSuffix(" Hz")
        self.windowLengthIntBox = QSpinBox()
        self.windowLengthIntBox.setRange(1, 10000000)
        self.windowLengthIntBox.setValue(10)
        self.windowLengthFloatBox = QDoubleSpinBox()
        self.windowLengthFloatBox.setRange(0.000000001, 10000000)
        self.windowLengthFloatBox.setValue(0.1)
        self.windowLengthFloatBox.setSuffix(" s")

        self.typeComboBox.currentIndexChanged.connect(self.updateUi)
        self.samplingRateBox.valueChanged.connect(self.updateSampleRate)
        self.windowLengthIntBox.valueChanged.connect(self.updateUi)
        self.windowLengthFloatBox.valueChanged.connect(self.updateUi)

        grid = QGridLayout()
        grid.addWidget(instructionLabel, 0, 0, 1, 2)
        grid.addWidget(line, 1, 0, 1, 2)
        grid.addWidget(typeLabel, 2, 0)
        grid.addWidget(samplingRateLabel, 3, 0)
        grid.addWidget(windowLengthLabel, 4, 0)
        grid.addWidget(self.typeComboBox, 2, 1)
        grid.addWidget(self.samplingRateBox, 3, 1)
        grid.addWidget(self.windowLengthIntBox, 4, 1)
        grid.addWidget(self.windowLengthFloatBox, 4, 1)
        self.windowLengthFloatBox.hide()
        self.setLayout(grid)

        self.updateUi()

    def updateSampleRate(self):
        if self.oldSampleRate is 0 and self.samplingRateBox.value() is not 0:
            self.windowLengthIntBox.hide()
            self.windowLengthFloatBox.show()
        elif self.oldSampleRate is not 0 and self.samplingRateBox.value() is 0:
            self.windowLengthIntBox.show()
            self.windowLengthFloatBox.hide()
        self.oldSampleRate = self.samplingRateBox.value()
        self.updateUi()

    def updateUi(self):
        self.valuesChanged.emit()

    def returnFunction(self):
        self._type = self.filterTypes[self.typeComboBox.currentText()]
        self.samplingRate = self.samplingRateBox.value()
        if self.samplingRate is 0:
            length = self.windowLengthIntBox.value()
            if (length % 2 == 0):  # Number must be odd for sig. processing
                length += 1
            self.windowLength = length
        else:
            self.windowLength = self.windowLengthFloatBox.value()
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
        elif self._type == 'max':
            m = ts.RollingMax(self.windowLength, self.samplingRate)
            signal = list(m.roll(y, end=True))
        else:
            raise ValueError("Filter function {} not found.".format(self._type))
        signal = np.asarray(signal)
        data = (x, signal)
        return data
