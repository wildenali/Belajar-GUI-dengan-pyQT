#!/usr/bin/python3

# Membuat GUI sederhana

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

if __name__== '__main__':
    a = QApplication(sys.argv)

    form = QWidget()
    form.resize(300,200)
    form.move(300,300)
    form.setWindowTitle('GUI Sederhana')

    label = QLabel('Hayy hay... cek')
    label.move(55,40)
    label.setParent(form)

    form.show()

    a.exec_()
