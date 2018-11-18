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
        self.resize(700,200)
        self.move(300,300)
        self.setWindowTitle('Slider dan LCD Display')

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(-101)
        self.slider.setMaximum(101)
        self.slider.setValue(10)

        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(4)
        self.lcd.display(10)

        layout = QVBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(self.lcd)
        self.setLayout(layout)

        self.slider.sliderMoved.connect(self.sliderMoved)

    def sliderMoved(self):
        self.lcd.display(self.slider.value())

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
