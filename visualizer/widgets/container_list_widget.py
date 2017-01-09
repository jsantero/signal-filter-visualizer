from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ContainerListWidget(QWidget):
    def __init__(self, container):
        super().__init__()
        self.listWidget = QListWidget()
        self.container = container
        removeButton = QPushButton("Remove")

        grid = QGridLayout()
        grid.addWidget(self.listWidget, 0, 0, 3, 1)
        grid.addWidget(removeButton, 0, 4, 1, 1)
        self.setLayout(grid)

        removeButton.clicked.connect(self.remove)

    def add(self, element):
        self.container.add(element)
        self.listWidget.addItem(element.name)

    def remove(self):
        index = self.listWidget.currentRow()
        self.container.remove(index)
        self.listWidget.takeItem(index)
