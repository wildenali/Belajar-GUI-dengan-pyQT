#!/usr/bin/python3

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QDialog):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(300,300)
        self.move(300,300)
        self.setWindowTitle('QMessageBox')

        self.aboutButton = QPushButton('About')
        self.criticalButton = QPushButton('Critical')
        self.informationButton = QPushButton('Information')
        self.questionButton = QPushButton('Question')
        self.warningButton = QPushButton('Warning')

        layout = QHBoxLayout()
        layout.addWidget(self.aboutButton)
        layout.addWidget(self.criticalButton)
        layout.addWidget(self.informationButton)
        layout.addWidget(self.questionButton)
        layout.addWidget(self.warningButton)
        self.setLayout(layout)

        self.aboutButton.clicked.connect(self.aboutButtonClick)
        self.criticalButton.clicked.connect(self.criticalButtonClick)
        self.informationButton.clicked.connect(self.informationButtonClick)
        self.questionButton.clicked.connect(self.questionButtonClick)
        self.warningButton.clicked.connect(self.warningButtonClick)

    def aboutButtonClick(self):
        QMessageBox.about(self, 'Tentang Program', 'Video Recorder\n' + 'Versi 1.0.0\n' + 'Hak Cipta (c)')

    def criticalButtonClick(self):
        QMessageBox.critical(self, 'Kesalahan', 'File anu tidak ditemukan')

    def informationButtonClick(self):
        QMessageBox.information(self, 'Informasi', 'Proses telah selesai dilakukan')

    def questionButtonClick(self):
        fileName = 'settings.conf'
        response = QMessageBox.question(self, 'Konfirmasi', 'Anda yakin akan menghapus file %s?' %fileName)

        if response == QMessageBox.Yes:
            QMessageBox.about(self, 'Respon', 'Anda Memilih YEEES')
        else:
            QMessageBox.about(self, 'Respon', 'Anda Memilih NOOOOO')

    def warningButtonClick(self):
        QMessageBox.warning(self, 'Peringatan', 'Apakan ANDA mau MENGHAPUS SEMUA DATANYA?')

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
