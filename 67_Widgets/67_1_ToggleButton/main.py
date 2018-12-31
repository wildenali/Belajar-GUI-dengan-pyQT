#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QFrame, QApplication
from PyQt5.QtGui import QColor

class toggleButton(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.col = QColor(0, 0, 0)

        redButton = QPushButton('Red', self)
        redButton.setCheckable(True)
        redButton.move(10, 10)
        redButton.clicked[bool].connect(self.setColor)

        greenButton = QPushButton('Green', self)
        greenButton.setCheckable(True)
        greenButton.move(10, 60)
        greenButton.clicked[bool].connect(self.setColor)

        blueButton = QPushButton('Blue', self)
        blueButton.setCheckable(True)
        blueButton.move(10, 110)
        blueButton.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget {background-color: %s}" % self.col.name())

        self.setGeometry(500, 300, 280, 170)
        self.setWindowTitle('Toggle Button')
        self.show()

    def setColor(self, pressed):
        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet("QFrame {background-color: %s}" % self.col.name())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = toggleButton()
    sys.exit(app.exec_())
