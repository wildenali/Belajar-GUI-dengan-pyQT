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
        self.resize(300,200)
        self.move(300,300)
        self.setWindowTitle('ComboBox')

        self.combo = QComboBox()
        for i in range(1,11):
            self.combo.addItem('Item ke-%d' %i)

        self.getTextButton = QPushButton('Ambil Teks')

        layout = QVBoxLayout()
        layout.addWidget(self.combo)
        layout.addWidget(self.getTextButton)
        layout.addStretch()
        self.setLayout(layout)

        self.getTextButton.clicked.connect(self.getTextButtonClick)

    def getTextButtonClick(self):
        QMessageBox.information(self, 'Informasi', 'Anda Memilih: ' + self.combo.currentText())

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
