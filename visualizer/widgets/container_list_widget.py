from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ContainerListWidget(QWidget):
    def __init__(self, container):
        super().__init__()
        self.listWidget = QListWidget()
        self.container = container

        grid = QGridLayout()
        grid.addWidget(self.listWidget)
        self.setLayout(grid)

    def add(self, element):
        self.container.add(element)
        self.listWidget.addItem(element.name)
