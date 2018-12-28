#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication

class boxLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        okButton = QPushButton("Ok")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(500, 250, 300, 150)
        self.setWindowTitle("Posisi Tombol pakai Layout")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainForm = boxLayout()
    sys.exit(app.exec_())
