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
        self.resize(500,300)
        self.move(300,300)
        self.setWindowTitle('Akses File dengan QFile')

        self.label1 = QLabel('Nama file')
        self.fileEdit = QLineEdit()
        self.label2 = QLabel('Data yang akan ditulis')
        self.inputTextEdit = QTextEdit()
        self.label3 = QLabel('Data yang akan dibaca')
        self.outputTextEdit = QTextEdit()
        self.outputTextEdit.setReadOnly(True)

        self.writeButton = QPushButton('Tulis Data')
        self.readButton = QPushButton('Baca Data')
        self.readButton.setDisabled(True)
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.writeButton)
        hbox.addWidget(self.readButton)

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.fileEdit)
        layout.addWidget(self.label2)
        layout.addWidget(self.inputTextEdit)
        layout.addWidget(self.label3)
        layout.addWidget(self.outputTextEdit)
        layout.addLayout(hbox)
        self.setLayout(layout)

        self.writeButton.clicked.connect(self.writeButtonClick)
        self.readButton.clicked.connect(self.readButtonClick)

    def writeButtonClick(self):
        if len(self.fileEdit.text().strip()) == 0:
            QMessage.critical(self, 'Kesalahan', 'Nama file isi dulu dong')
            return
        if self.inputTextEdit.document().isEmpty():
            QMessage.critical(self, 'Kesalahan', 'Data yang akan ditulis harus di isi')
            return
        # Menggunakan QFile
        f = QFile(self.fileEdit.text())
        if not f.open(QIODevice.WriteOnly | QIODevice.Text):
            return
        inputStream = QTextStream(f)
        inputStream << self.inputTextEdit.document().toPlainText()
        f.close()

        self.fileEdit.setDisabled(True)
        self.inputTextEdit.setDisabled(True)
        self.writeButton.setDisabled(True)
        self.readButton.setDisabled(False)

    def readButtonClick(self):
        f = QFile(self.fileEdit.text())
        if not f.open(QIODevice.ReadOnly | QIODevice.Text):
            return
        self.outputTextEdit.document().setPlainText(''.join(f.readAll()))
        f.close()

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
