#!/usr/bin/python3

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QDialog):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(500,450)
        self.move(300,100)
        self.setWindowTitle('Memilih File')

        self.textEdit = QTextEdit()

        self.openButton = QPushButton('Buka')
        hbox = QHBoxLayout()
        hbox.addWidget(self.openButton)
        hbox.addStretch()

        self.fileLabel = QLabel('Nama File: ')

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addLayout(hbox)
        layout.addWidget(self.fileLabel)
        self.setLayout(layout)

        self.openButton.clicked.connect(self.openButtonClick)

    def openButtonClick(self):
        import os
        fileName = QFileDialog.getOpenFileName(self, 'Pilih File nyaaa', os.curdir, 'Python Code (*.py);; Ruby Code (*.rb)', '*.py')

        if not fileName[0]: return
        self.fileLabel.setText('Nama file: ' + fileName[0])
        fileHandle = QFile(fileName[0])
        if not fileHandle.open(QIODevice.ReadOnly): return
        stream = QTextStream(fileHandle)
        self.textEdit.setPlainText(stream.readAll())
        fileHandle.close()

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
