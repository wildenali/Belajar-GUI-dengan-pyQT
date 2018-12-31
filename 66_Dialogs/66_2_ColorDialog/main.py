#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QFrame, QColorDialog, QApplication
from PyQt5.QtGui import QColor

class inputDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        col = QColor(0, 0, 0)
        self.button = QPushButton('Pilih Warna', self)
        self.button.move(20, 20)

        self.button.clicked.connect(self.showDialog)

        self.frame = QFrame(self)
        self.frame.setStyleSheet("QWidget {background-color: %s}" % col.name())
        self.frame.setGeometry(130, 22, 100, 100)

        self.setGeometry(500, 250, 250, 180)
        self.setWindowTitle('Color Dialog')
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.frame.setStyleSheet("QWidget {background-color: %s }" % col.name())

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = inputDialog()

    sys.exit(app.exec_())
