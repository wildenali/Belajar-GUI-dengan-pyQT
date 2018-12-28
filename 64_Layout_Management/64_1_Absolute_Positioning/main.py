#!/usr/bin/pyhton3

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

class absolutePositioning(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        label1 = QLabel('Satu', self)
        label1.move(15, 10)

        label2 = QLabel('Dua', self)
        label2.move(35, 40)

        label3 = QLabel('Tiga', self)
        label3.move(55, 70)

        self.setGeometry(500, 250, 250, 150)
        self.setWindowTitle('Absolute Positioning')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainApp = absolutePositioning()
    sys.exit(app.exec_())
