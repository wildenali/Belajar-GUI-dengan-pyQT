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
        self.setWindowTitle('FontComboBox')

        self.fontCombo = QComboBox()
        self.fontCombo.setEditable(True)

        self.label = QLabel('Contoh Teks')
        self.label.setFont(QFont('DejaVu Sans',18))

        layout = QVBoxLayout()
        layout.addWidget(self.fontCombo)
        layout.addWidget(self.label)
        layout.addStretch()
        self.setLayout(layout)

        self.fontCombo.activated.connect(self.fontComboBoxActivated)

    def fontComboBoxActivated(self):
        self.label.setFont(QFont(self.fontCombo.currentText(), 18))

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
