#!/usr/bin/python3

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QWidget):
    def __init__(self):
        super(MainForm, self).__init__()
        self.timer = QTimer()
        self.timer.setInterval(1000)    # 1 detik
        self.setupUI()
        self.timer.start()

    def setupUI(self):
        self.resize(600,300)
        self.move(300,300)
        self.setWindowTitle('QTimer')

        font = QFont()
        font.setFamily('SansSerif')
        font.setPixelSize(30)

        self.label = QLabel()
        self.label.setFont(font)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.timer.timeout.connect(self.timerTimer)

    def timerTimer(self):
        currentTimer = QTime.currentTime()
        self.label.setText(currentTimer.toString())

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
