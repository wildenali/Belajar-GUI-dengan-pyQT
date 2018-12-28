#!/usr/bin/python3

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication

class LCDDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        lcd = QLCDNumber(self)
        slider = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(slider)

        self.setLayout(vbox)
        slider.valueChanged.connect(lcd.display)

        self.setGeometry(500, 250, 250, 150)
        self.setWindowTitle('Signal dan Slot')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainForm = LCDDisplay()
    sys.exit(app.exec_())
