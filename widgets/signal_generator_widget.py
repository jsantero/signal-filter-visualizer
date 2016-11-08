from math import pi

import numpy as np

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class SignalGenerator(QWidget):

    generatorChanged = pyqtSignal(tuple)

    def __init__(self, parent=None):
        super().__init__(parent)

        amplitudeLabel = QLabel("Amplitude")
        freqAngularLabel = QLabel("Angular Frequency")
        freqLabel = QLabel("Frequency")
        phaseLabel = QLabel("Phase")
        samplesLabel = QLabel("Samples")

        self.amplitudeBox = QDoubleSpinBox()
        self.freqBox = QDoubleSpinBox()
        self.phaseBox = QDoubleSpinBox()
        self.samplesBox = QSpinBox()
        self.samplingRateBox = QSpinBox()
        self.amplitudeBox.setRange(-1000000.0, 1000000.0)
        self.amplitudeBox.setSuffix(" V")
        self.amplitudeBox.setValue(1.0)
        self.freqBox.setRange(0.0, 10000000000.0)
        self.freqBox.setSuffix(" Hz")
        self.freqBox.setValue(1.0)
        self.phaseBox.setRange(-2 * pi, 2 * pi)
        self.phaseBox.setSuffix(" rad")
        self.phaseBox.setValue(0.0)
        self.samplesBox.setRange(0, 100000)
        self.samplesBox.setValue(8000)

        self.listWidget = QListWidget()  # For showing user-defined signals

        addButton = QPushButton("Add")
        removeButton = QPushButton("Remove")

        amplitudeLabel.setBuddy(self.amplitudeBox)
        freqLabel.setBuddy(self.freqBox)
        phaseLabel.setBuddy(self.phaseBox)
        samplesLabel.setBuddy(self.samplesBox)

        addButton.clicked.connect(self.addNewSignal)
        removeButton.clicked.connect(self.removeSignal)

        grid = QGridLayout()
        grid.addWidget(amplitudeLabel, 0, 0)
        grid.addWidget(freqLabel, 1, 0)
        grid.addWidget(phaseLabel, 2, 0)
        grid.addWidget(samplesLabel, 3, 0)
        grid.addWidget(self.amplitudeBox, 0, 1)
        grid.addWidget(self.freqBox, 1, 1)
        grid.addWidget(self.phaseBox, 2, 1)
        grid.addWidget(self.samplesBox, 3, 1)
        grid.addWidget(addButton, 4, 0)
        grid.addWidget(removeButton, 4, 2)
        grid.addWidget(self.listWidget, 0, 2, 4, 2)
        self.setLayout(grid)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)

        self.signalDict = {}  # Stores user-defined signals

    def addNewSignal(self):
        a = self.amplitudeBox.value()
        f0 = self.freqBox.value()
        phi = self.phaseBox.value()
        n = self.samplesBox.value()

        x = np.linspace(- 1, 1, n)
        y = a * np.sin(2 * pi * f0 * x + phi)

        key = "{}*sin(2*pi*{}+{})".format(a, f0, phi)
        if key not in self.signalDict:
            self.signalDict[key] = y
            self.listWidget.addItem(key)
            self.listWidget.sortItems()

        self.updateGenerator()

    def removeSignal(self):
        item = self.listWidget.takeItem(self.listWidget.currentRow())
        if item:
            self.signalDict.pop(item.text())
        self.updateGenerator()

    def updateGenerator(self):
        n = self.samplesBox.value()
        x = np.linspace(- 1, 1, n)
        y = 0
        for key, value in self.signalDict.items():
            y += value
        data = (x,y)
        self.generatorChanged.emit(data)
