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
        self.resize(400,100)
        self.move(300,200)
        self.setWindowTitle('Menghapus File')

        self.label1 = QLabel('Nama File yang akan di hapus')
        self.fileEdit = QLineEdit()
        self.removeButton = QPushButton('Hapuuuus')
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.removeButton)

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.fileEdit)
        layout.addStretch()
        layout.addLayout(hbox)
        self.setLayout(layout)

        self.removeButton.clicked.connect(self.removeButtonClick)

    def removeButtonClick(self):
        if len(self.fileEdit.text().strip()) == 0:
            QMessageBox.critical(self, 'Kesalahan', 'Nama File Harus di isi')
            return
        if not QFile.exists(self.fileEdit.text()):
            return

        # menghapus file
        fileName = self.fileEdit.text()
        if QFile.remove(fileName):
            QMessageBox.information(self, 'informasi', 'file "%s" telah di hapus' % fileName)
        else:
            QMessageBox.information(self, 'informasi', 'tidak ada file yang di hapus')

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
