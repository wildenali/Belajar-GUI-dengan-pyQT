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
        self.resize(800,400)
        self.move(300,100)
        self.setWindowTitle('Table Widget')


if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
