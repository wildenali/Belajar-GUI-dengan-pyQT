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
        self.move(500,100)
        self.setWindowTitle('Mengubah WARNA')

        self.textEdit = QTextEdit()

        self.colorButton = QPushButton('Pilih Warna')

        hbox = QHBoxLayout()
        hbox.addWidget(self.colorButton)
        hbox.addStretch()

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addLayout(hbox)
        self.setLayout(layout)

        self.colorButton.clicked.connect(self.colorButtonClick)

    def colorButtonClick(self):
        color = QColorDialog.getColor(Qt.red, self, 'Pilih Warna')
        if color:
            self.textEdit.setTextColor(color)

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
