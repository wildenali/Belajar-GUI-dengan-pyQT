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
        self.resize(400,150)
        self.move(300,300)
        self.setWindowTitle('Menyalin File')

        self.label1 = QLabel('Nama file yang mau di copy')
        self.sourceFileEdit = QLineEdit()
        self.label2 = QLabel('Nama file Salinan')
        self.destFileEdit = QLineEdit()
        self.copyButton = QPushButton('Ngopi')

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.copyButton)

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.sourceFileEdit)
        layout.addWidget(self.label2)
        layout.addWidget(self.destFileEdit)
        layout.addStretch()
        layout.addLayout(hbox)
        self.setLayout(layout)

        self.copyButton.clicked.connect(self.copyButtonClick)

    def copyButtonClick(self):
        if len(self.sourceFileEdit.text().strip()) == 0 or len(self.destFileEdit.text().strip()) == 0:
            QMessageBox.critical(self, 'Kesalahan', 'Nama file yang mau di copy dan tempat penyimpanan harus di isi')
            return
        if not QFile.exists(self.sourceFileEdit.text()):
            return

        # Menyalin file menggunakan QFile
        sourceFile = self.sourceFileEdit.text()
        destFile = self.destFileEdit.text()
        if QFile.copy(sourceFile, destFile):
            QMessageBox.information(self, 'informasi', 'File berhasil di copy')
        else:
            QMessageBox.information(self, 'informasi', 'File Gagal di copy')

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
