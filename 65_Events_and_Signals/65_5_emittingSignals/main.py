#!/usr/bin/python3

#ini kalau di klik si apps nya, dia bakal nge close

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication

class communicate(QObject):
    closeApp = pyqtSignal()

class emmitingSignals(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.c = communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(500, 250, 290, 150)
        self.setWindowTitle('Emit Signal')
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = emmitingSignals()
    sys.exit(app.exec_())
