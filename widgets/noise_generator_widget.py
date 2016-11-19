import numpy as np

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class NoiseGenerator(QWidget):

    noiseAdded = pyqtSignal(tuple)

    def __init__(self, parent=None):
        super().__init__()

        checkLabel = QLabel("Add Noise")
        meanLabel = QLabel("Noise mean")
        deviationLabel = QLabel("Standard Deviation")

        self.checkBox = QCheckBox()
        self.checkBox.setTristate(False)
        self.checkBox.setChecked(False)
        self.meanBox = QDoubleSpinBox()
        self.meanBox.setRange(-1000000.0, 1000000.0)
        self.meanBox.setDecimals(4)
        self.meanBox.setValue(0.0)
        self.deviationBox = QDoubleSpinBox()
        self.deviationBox.setRange(0.0001, 1000000.0)
        self.deviationBox.setDecimals(4)
        self.deviationBox.setValue(1)

        meanLabel.setBuddy(self.meanBox)
        deviationLabel.setBuddy(self.deviationBox)
        checkLabel.setBuddy(self.checkBox)

        self.checkBox.stateChanged.connect(self.updateUi)
        self.meanBox.valueChanged.connect(self.updateUi)
        self.deviationBox.valueChanged.connect(self.updateUi)

        grid = QGridLayout()
        grid.addWidget(checkLabel, 0, 0)
        grid.addWidget(self.checkBox, 0, 1)
        grid.addWidget(meanLabel, 1, 0)
        grid.addWidget(deviationLabel, 2, 0)
        grid.addWidget(self.meanBox, 1, 1)
        grid.addWidget(self.deviationBox, 2 ,1)
        self.setLayout(grid)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)

        # Stores the last generated signal so a new filter can be re-applied
        # without re-generating previous signal
        self.latestData = None

    def updateUi(self):
        if self.latestData:  # Only add noise if data exists to be noised
            self.addNoise(self.latestData)

    def addNoise(self, data):
        self.latestData = data
        if self.checkBox.checkState():
            x, y = self.latestData
            if x is not 0 and y is not 0:
                mean = self.meanBox.value()
                deviation = self.deviationBox.value()
                length = len(y)

                noise = np.random.normal(mean, deviation, length)
                data = (x, y + noise)  # Add noise to generated data
        else: data = self.latestData
        self.noiseAdded.emit(data)
