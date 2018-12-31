#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication
from PyQt5.QtCore import QBasicTimer

class progressBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(30, 40, 200, 25)

        self.button = QPushButton('Start', self)
        self.button.move(40, 80)
        self.button.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(500, 300, 280, 170)
        self.setWindowTitle("QProgressBar")
        self.show()

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.button.setText('Finished')
            return

        self.step = self.step + 1
        self.progressBar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.button.setText('Start')
        else:
            self.timer.start(100, self)
            self.button.setText('Stop')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = progressBar()
    sys.exit(app.exec_())
