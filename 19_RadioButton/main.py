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
        self.resize(400,150)
        self.move(300,300)
        self.setWindowTitle('Contoh Radio Button')

        self.label1 = QLabel()
        self.label1.setText('Bilangan Pertama')
        self.numberEdit1 = QLineEdit()
        self.label2 = QLabel()
        self.label2.setText('Bilangan Kedua')
        self.numberEdit2 = QLineEdit()
        grid = QGridLayout()
        grid.addWidget(self.label1, 0, 0)
        grid.addWidget(self.numberEdit1, 0, 1)
        grid.addWidget(self.label2, 1, 0)
        grid.addWidget(self.numberEdit2, 1, 1)

        self.addRadio = QRadioButton()
        self.addRadio.setText('&Tambah')
        self.addRadio.setChecked(True)
        self.substractRadio = QRadioButton()
        self.substractRadio.setText('&Kurang')
        self.mulRadio = QRadioButton()
        self.mulRadio.setText('&Kali')
        self.divRadio = QRadioButton()
        self.divRadio.setText('&Bagi')
        hbox = QHBoxLayout()
        hbox.addWidget(self.addRadio)
        hbox.addWidget(self.substractRadio)
        hbox.addWidget(self.mulRadio)
        hbox.addWidget(self.divRadio)

        self.resultLabel = QLabel('<b>hasil Penjumlahan: </b>')

        self.calculationButton = QPushButton('Berapa ya')

        layout = QVBoxLayout()
        layout.addLayout(grid)
        layout.addLayout(hbox)
        layout.addWidget(self.resultLabel)
        layout.addWidget(self.calculationButton)
        layout.addStretch()
        self.setLayout(layout)

        self.addRadio.clicked.connect(lambda: self.resultLabel.setText('<b>Hasil Penjumlahan: </b>'))
        self.substractRadio.clicked.connect(lambda: self.resultLabel.setText('<b>Hasil Pengurangan: </b>'))
        self.mulRadio.clicked.connect(lambda: self.resultLabel.setText('<b>Hasil Perkalian: </b>'))
        self.divRadio.clicked.connect(lambda: self.resultLabel.setText('<b>Hasil Pembagian: </b>'))

        self.calculationButton.clicked.connect(self.calculationButtonClick)

    def calculationButtonClick(self):
        a = float(self.numberEdit1.text())
        b = float(self.numberEdit2.text())

        if self.addRadio.isChecked(): c = a + b
        elif self.substractRadio.isChecked(): c = a - b
        elif self.mulRadio.isChecked(): c = a * b
        else: c = a / b

        index = str(self.resultLabel.text()).index(':')
        s = str(self.resultLabel.text())[:index+1]
        self.resultLabel.setText('%s %.2f %s' % (s, c, '</b>'))

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
