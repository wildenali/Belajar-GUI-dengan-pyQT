#!/usr/bin/python3

import sys
from mainform import *
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
