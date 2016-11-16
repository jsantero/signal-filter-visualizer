from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class FileOpenDlg(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Open data file")

        self.fileDlg = QFileDialog(self)
        fileLabel = QLabel("File")
        sampleRateLabel = QLabel("Samplerate")

        self.fileBox = QLabel()
        self.sampleRateBox = QSpinBox()
        self.sampleRateBox.setRange(1, 100000)
        self.sampleRateBox.setValue(100)

        grid = QGridLayout()
        grid.addWidget(fileLabel, 0, 0)
        grid.addWidget(self.fileBox, 0, 1)
        grid.addWidget(sampleRateLabel, 1, 0)
        grid.addWidget(self.sampleRateBox, 1, 1)
        self.setLayout(grid)

        if self.fileDlg.exec_():
            filenames = self.fileDlg.selectedFiles()
            self.fileBox.setText(filenames[0])
            print(filenames)
