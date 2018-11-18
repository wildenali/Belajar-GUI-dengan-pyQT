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
        self.resize(400,400)
        self.move(300,100)
        self.setWindowTitle('Progress Bar')

        self.label1 = QLabel('Bilangan Ganjil')
        self.list1 = QListWidget()

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.label1)
        vbox1.addWidget(self.list1)

        self.label2 = QLabel('Bilangan Genap')
        self.list2 = QListWidget()

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.label2)
        vbox2.addWidget(self.list2)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2)

        self.progress = QProgressBar()
        self.progress.setMinimum(0)
        self.progress.setMaximum(1000)
        self.progress.setValue(0)

        self.startButton = QPushButton('Mulai...')

        layout = QVBoxLayout()
        layout.addLayout(hbox)
        layout.addWidget(self.progress)
        layout.addWidget(self.startButton)
        self.setLayout(layout)

        self.startButton.clicked.connect(self.startButtonClick)

    def startButtonClick(self):
        self.progress.setValue(0)
        for i in range(0,1000):
            QApplication.processEvents()
            if i % 2 == 1: self.list1.addItem(str(i))
            else: self.list2.addItem(str(i))
            self.progress.setValue(self.progress.value() + 1)

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
