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
        self.resize(900,100)
        self.move(300,300)
        self.setWindowTitle('CheckBox dengan Flag')

        self.label1 = QLabel()
        self.label1.setText('Nama File:')

        self.fileName = '/home/password-sari/Documents/#github wilden/Belajar-GUI-dengan-pyQT/21_CheckBoxwithFlag/main.py'

        self.lineEdit = QLineEdit(self.fileName)
        self.fullPathCheck = QCheckBox()
        self.fullPathCheck.setText('Nama file disertai path lengkap')
        self.fullPathCheck.setChecked(True)

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.fullPathCheck)
        layout.addStretch()
        self.setLayout(layout)

        self.fullPathCheck.clicked.connect(self.fullPathCheckClick)

    def fullPathCheckClick(self):
        if self.fullPathCheck.isChecked(): self.lineEdit.setText(self.fileName)
        else:
            import ntpath
            s = ntpath.basename(self.fileName)
            self.lineEdit.setText(s)

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
