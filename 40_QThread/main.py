#!/usr/bin/python3

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# Kelas turunan dari QThread
class MyThread(QThread):
    def __init__(self, name, listWidget):
        super(MyThread, self).__init__()
        self.name = name
        self.listWidget = listWidget
    # override metode run()
    def run(self):
        for i in range(1, 10000):
            self.listWidget.addItem(self.name + ': ' +str(i))

class MainForm(QWidget):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUI()

        # Membuat objek dari kelas MyThread
        self.thread1 = MyThread('Thread 1', self.listWidget)
        self.thread2 = MyThread('Thread 2', self.listWidget)

    def setupUI(self):
        self.resize(300,300)
        self.move(300,300)
        self.setWindowTitle('QThread')

        self.listWidget = QListWidget()
        self.startButton = QPushButton('Mulai')
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.startButton)

        layout = QVBoxLayout()
        layout.addWidget(self.listWidget)
        layout.addLayout(hbox)
        self.setLayout(layout)

        self.startButton.clicked.connect(self.startButtonClick)

    def startButtonClick(self):
        QApplication.processEvents()
        self.thread1.start()
        self.thread2.start()

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
