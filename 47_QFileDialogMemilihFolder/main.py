#!/usr/bin/python3

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QWidget):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(500,450)
        self.move(400,100)
        self.setWindowTitle('QFileDialog getExistingDirectory()')

        self.lineEdit = QLineEdit()
        self.dirButton = QPushButton('Pilih Folder')
        hbox = QHBoxLayout()
        hbox.addWidget(self.lineEdit)
        hbox.addWidget(self.dirButton)

        self.treeView = QTreeView()
        layout = QVBoxLayout()
        layout.addLayout(hbox)
        layout.addWidget(self.treeView)
        self.setLayout(layout)

        self.dirButton.clicked.connect(self.dirButtonClick)

    def dirButtonClick(self):
        import os
        dirName = QFileDialog.getExistingDirectory(self, 'Pilih Folder', os.curdir, QFileDialog.ShowDirsOnly)
        if not dirName: return
        self.lineEdit.setText(dirName)
        model = QFileSystemModel()
        model.setRootPath(dirName)
        model.setFilter(QDir.AllDirs | QDir.Files)
        self.treeView.setModel(model)
        self.treeView.setRootIndex(model.index(dirName))

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
