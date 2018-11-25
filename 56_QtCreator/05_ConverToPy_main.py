#!/usr/bin/python3

import sys

from ConvertToPy import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.helloButton.clicked.connect(self.helloButtonClick)

    def helloButtonClick(self):
        QMessageBox.information(self, 'Informasi', 'Hallo %s, Apa Kabar?' % self.ui.nameEdit.text())

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
