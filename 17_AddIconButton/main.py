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
        self.setWindowTitle('Icon di Button')

        self.label = QLabel()
        self.label.setText('Tambahin Icon di Button')

        icon1 = QIcon('addicon.png')
        self.button1 = QPushButton('\tTambah')
        self.button1.setIcon(icon1)

        icon2 = QIcon('deleteicon.png')
        self.button2 = QPushButton('\tHapuuus')
        self.button2.setIcon(icon2)

        icon3 = QIcon('refreshicon.png')
        self.button3 = QPushButton('Refresh')
        self.button3.setIcon(icon3)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addLayout(hbox)
        self.setLayout(layout)

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
