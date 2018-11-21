#!/usr/bin/python3

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class DialogForm(QDialog):
    def __init__(self):
        super(DialogForm, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(300,300)
        self.move(300,300)
        self.setWindowTitle('Dialog')

        self.label = QLabel('')

        self.closeButton = QPushButton('Keluar')

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.closeButton)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addLayout(hbox)
        self.setLayout(layout)

        self.closeButton.clicked.connect(self.close)


class MainForm(QWidget):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(300,100)
        self.move(400,400)
        self.setWindowTitle('QDialog.setModal()')

        self.label = QLabel('Tulis Teks pada Kotak dibawah ini')
        self.lineEdit = QLineEdit()
        self.showModalDialogButton = QPushButton('Modal')
        self.showModelessDialogButton = QPushButton('non-Modal')

        hbox = QHBoxLayout()
        hbox.addWidget(self.showModalDialogButton)
        hbox.addWidget(self.showModelessDialogButton)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.lineEdit)
        layout.addLayout(hbox)
        self.setLayout(layout)

        self.showModalDialogButton.clicked.connect(self.showModalDialogButtonClick)
        self.showModelessDialogButton.clicked.connect(self.showModelessDialogButtonClick)

    def showModalDialogButtonClick(self):
        self.form = DialogForm()
        self.form.label.setText('Dialog bersifat MODAL')
        self.form.setModal(True)
        self.form.show()

    def showModelessDialogButtonClick(self):
        self.form = DialogForm()
        self.form.label.setText('Dialog bersifat non-MODAL (modeless)')
        self.form.setModal(False)
        self.form.show()

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
