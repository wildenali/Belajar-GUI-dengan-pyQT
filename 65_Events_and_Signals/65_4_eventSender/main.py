#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

class eventSender(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        button1 = QPushButton("Tombol 1", self)
        button1.move(30, 50)

        button2 = QPushButton("Tombol 2", self)
        button2.move(150, 50)

        button1.clicked.connect(self.buttonClicked)
        button2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(500, 250, 290, 150)
        self.setWindowTitle('Event Sender')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' ditekan')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = eventSender()
    sys.exit(app.exec_())
