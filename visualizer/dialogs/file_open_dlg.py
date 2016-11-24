import os.path

import numpy as np

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from visualizer.classes.signalchain import ChainElement

class SignalLoaderDlg(QDialog):

    #signalReady = pyqtSignal(tuple)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Load File")

        self.fileDlg = QFileDialog(self)
        selectButton = QPushButton("Load file")
        self.fileBox = QLabel()
        sampleRateLabel = QLabel("Samplerate")

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok|
                                     QDialogButtonBox.Cancel)
        buttonBox.button(QDialogButtonBox.Ok).setDefault(True)

        self.fileBox = QLabel()
        self.sampleRateBox = QSpinBox()
        self.sampleRateBox.setRange(1, 100000)
        self.sampleRateBox.setValue(100)

        selectButton.clicked.connect(self.selectPressed)
        buttonBox.accepted.connect(self.loadFile)
        buttonBox.rejected.connect(self.reject)

        grid = QGridLayout()
        grid.addWidget(sampleRateLabel, 0, 0)
        grid.addWidget(self.sampleRateBox, 0, 1)
        grid.addWidget(selectButton, 1, 0)
        grid.addWidget(self.fileBox, 1, 1)
        grid.addWidget(buttonBox, 2, 0, 1, 2)
        self.setLayout(grid)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)

    def selectPressed(self):
        if self.fileDlg.exec_():
            filenames = self.fileDlg.selectedFiles()
            self.fileBox.setText(filenames[0])

    def loadFile(self):
        path = self.fileBox.text()
        sampleRate = self.sampleRateBox.value()
        try:
            y = np.genfromtxt(path, delimiter=',')
            samples = len(y)
            t = samples / sampleRate
            x = np.linspace(0, t, samples)
            self.data = (x, y)
            name = os.path.basename(path)
            def function(input_):
                return (x, y)
            data = (0, 0)
            self.newElement = ChainElement(data=data, name=name)
            self.newElement.function = function
            self.newElement.update()
            self.accept()
            #self.signalReady.emit(data)
        except ValueError as e:
            print("File parse error: {}".format(e))
