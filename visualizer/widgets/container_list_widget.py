from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ContainerListWidget(QWidget):
    def __init__(self, container):
        super().__init__()
        self.listWidget = QListWidget()
        self.container = container
        renameButton = QPushButton("Rename")
        removeButton = QPushButton("Remove")

        grid = QGridLayout()
        grid.addWidget(self.listWidget, 0, 0, 3, 1)
        grid.addWidget(renameButton, 0, 4, 1, 1)
        grid.addWidget(removeButton, 1, 4, 1, 1)
        self.setLayout(grid)

        renameButton.clicked.connect(self.rename)
        removeButton.clicked.connect(self.remove)

    def add(self, element):
        self.container.add(element)
        self.listWidget.addItem(element.name)

    def remove(self):
        index = self.listWidget.currentRow()
        self.container.remove(index)
        self.listWidget.takeItem(index)

    def rename(self):
        if not self.listWidget.currentItem():
            return

        class RenameDlg(QDialog):
            def __init__(self, listWidget, container, parent=None):
                super().__init__()
                self.listWidget = listWidget
                self.container = container
                self.setWindowTitle("Rename")
                renameLabel = QLabel("Enter new name")
                self.lineEdit = QLineEdit()
                buttonBox = QDialogButtonBox(QDialogButtonBox.Ok |
                                             QDialogButtonBox.Cancel)

                grid = QGridLayout()
                grid.addWidget(renameLabel, 0, 0, 1, 2)
                grid.addWidget(self.lineEdit, 1, 0, 1, 2)
                grid.addWidget(buttonBox, 2, 0, 1, 2)
                self.setLayout(grid)

                buttonBox.accepted.connect(self.renameOk)
                buttonBox.rejected.connect(self.reject)

            def renameOk(self):
                name = self.lineEdit.text()
                target = self.listWidget.currentItem()
                target.setText(name)
                index = self.listWidget.currentRow()
                self.container.rename(index, name)

                self.lineEdit.clear()
                self.accept()

            def reject(self):
                self.accept()

        dlg = RenameDlg(self.listWidget, self.container, self)
        dlg.exec_()
