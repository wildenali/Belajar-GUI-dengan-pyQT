#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QWidget, QSlider, QLabel, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class slider(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        slider = QSlider(Qt.Horizontal, self)
        slider.setFocusPolicy(Qt.NoFocus)
        slider.setGeometry(30, 40, 100, 30)
        slider.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('mute.png'))
        self.label.setGeometry(160, 20, 80, 80)

        self.setGeometry(500, 300, 280, 170)
        self.setWindowTitle("QSlider")
        self.show()

    def changeValue(self, value):
        if value == 0:
            self.label.setPixmap(QPixmap('mute.png'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('min.png'))
        elif value > 30 and value <= 80:
            self.label.setPixmap(QPixmap('med.png'))
        else:
            self.label.setPixmap(QPixmap('max.png'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = slider()
    sys.exit(app.exec_())
