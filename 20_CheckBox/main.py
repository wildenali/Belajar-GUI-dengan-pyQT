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
        self.resize(400,100)
        self.move(300,300)
        self.setWindowTitle('Contoh Check Box')

        self.label1 = QLabel()
        self.label1.setText('Tentukan Pilihan Anda')

        self.cppCheck = QCheckBox()
        self.cppCheck.setText('C++')
        self.pythonCheck = QCheckBox()
        self.pythonCheck.setText('Python')
        self.javaCheck = QCheckBox()
        self.javaCheck.setText('Java')
        self.javascriptCheck = QCheckBox()
        self.javascriptCheck.setText('JavaScript')

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.cppCheck)
        hbox1.addWidget(self.pythonCheck)
        hbox1.addWidget(self.javaCheck)
        hbox1.addWidget(self.javascriptCheck)

        self.okButton = QPushButton('&OK')
        self.exitButton = QPushButton('&Ga Jadi')

        hbox2 = QHBoxLayout()
        hbox2.addStretch()
        hbox2.addWidget(self.okButton)
        hbox2.addWidget(self.exitButton)

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addLayout(hbox1)
        horizontaLine = QFrame()
        horizontaLine.setFrameShape(QFrame.HLine)
        horizontaLine.setFrameShadow(QFrame.Sunken)
        layout.addWidget(horizontaLine)
        layout.addLayout(hbox2)
        layout.addStretch()
        self.setLayout(layout)

        self.okButton.clicked.connect(self.okButtonClick)
        self.exitButton.clicked.connect(self.close)

    def okButtonClick(self):
        choices = []
        if self.cppCheck.isChecked(): choices.append('C++')
        if self.pythonCheck.isChecked(): choices.append('Python')
        if self.javaCheck.isChecked(): choices.append('Java')
        if self.javascriptCheck.isChecked(): choices.append('JavaScript')
        QMessageBox.information(self, 'Informasi', repr(choices))

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
