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
        self.resize(300,100)
        self.move(300,300)
        self.setWindowTitle('Form Dialog')

        self.label = QLabel('Form Dialog Kedua')

        self.okButton = QPushButton('Siip')
        self.cancelButton = QPushButton('Ga Jadi')

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.okButton)
        hbox.addWidget(self.cancelButton)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addLayout(hbox)
        self.setLayout(layout)

        self.okButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)


class MainForm(QWidget):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(300,100)
        self.move(200,100)
        self.setWindowTitle('QDialog.accept() dan QDialog.reject()')

        self.label = QLabel('Form UTAMA')
        self.showDialogButton = QPushButton('Tampilkan Dialog')

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.showDialogButton)
        self.setLayout(layout)

        self.showDialogButton.clicked.connect(self.showDialogButtonClick)

    def showDialogButtonClick(self):
        form = DialogForm()
        if form.exec_() == QDialog.Accepted:
            QMessageBox.information(self, 'Informasi', 'Anda memilik tombol Siip')
        else:
            QMessageBox.information(self, 'Informasi', 'Anda memilik tombol Ga Jadi')

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
