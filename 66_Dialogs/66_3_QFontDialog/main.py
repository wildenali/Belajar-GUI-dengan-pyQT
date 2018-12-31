#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QLabel, QFontDialog, QApplication

class fontDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):

        vbox = QVBoxLayout()

        button = QPushButton('Pilih Font', self)
        button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        button.move(20, 20)

        vbox.addWidget(button)

        button.clicked.connect(self.showDialog)

        self.label = QLabel('Knowlage only matters', self)
        self.label.move(130, 20)

        vbox.addWidget(self.label)
        self.setLayout(vbox)

        self.setGeometry(500, 250, 250, 180)
        self.setWindowTitle('Font Dialog')
        self.show()

    def showDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.label.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = fontDialog()

    sys.exit(app.exec_())
