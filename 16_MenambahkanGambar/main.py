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
        self.resize(400,200)
        self.move(300,300)
        self.setWindowTitle('Import Gambar')

        self.label1 = QLabel()
        self.label1.setText('Import Gambar dengan QLabel')

        # ========== Cara Pertama
        # self.label2 = QLabel()
        # self.label2.setText('<img src="gambarini.png">')
        # ========== End Cara Pertama

        # ========== Cara Kedua
        pixmap = QPixmap('gambaritu.png')
        self.label2 = QLabel()
        self.label2.setPixmap(pixmap)
        # ========== End Cara Kedua


        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        self.setLayout(layout)

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
