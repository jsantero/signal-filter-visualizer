import numpy as np

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class SignalLoaderDlg(QDialog):

    #signalReady = pyqtSignal(tuple)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.fileDlg = QFileDialog(self)
        selectButton = QPushButton("Load file")
        self.fileBox = QLabel()
        sampleRateLabel = QLabel("Samplerate")
        loadButton = QPushButton("Load file")

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok|
                                     QDialogButtonBox.Cancel)
        buttonBox.button(QDialogButtonBox.Ok).setDefault(True)

        self.fileBox = QLabel()
        self.sampleRateBox = QSpinBox()
        self.sampleRateBox.setRange(1, 100000)
        self.sampleRateBox.setValue(100)

        selectButton.clicked.connect(self.selectPressed)
        loadButton.clicked.connect(self.loadPressed)
        buttonBox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)

        grid = QGridLayout()
        grid.addWidget(selectButton, 0, 0)
        grid.addWidget(self.fileBox, 0, 1)
        grid.addWidget(sampleRateLabel, 1, 0)
        grid.addWidget(self.sampleRateBox, 1, 1)
        grid.addWidget(loadButton, 2, 0)
        grid.addWidget(buttonBox, 3, 0, 1, 2)
        self.setLayout(grid)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)

    def selectPressed(self):
        if self.fileDlg.exec_():
            filenames = self.fileDlg.selectedFiles()
            self.fileBox.setText(filenames[0])
            self.loadFile()

    def loadFile(self):
        path = self.fileBox.text()
        sampleRate = self.sampleRateBox.value()
        try:
            y = np.genfromtxt(path, delimiter=',')
            samples = len(y)
            t = samples / sampleRate
            x = np.linspace(0, t, samples)
            self.data = (x, y)
            #self.signalReady.emit(data)
        except ValueError as e:
            print("File parse error: {}".format(e))
