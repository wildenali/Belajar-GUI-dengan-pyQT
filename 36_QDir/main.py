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
        self.move(300,100)
        self.setWindowTitle('Membuar Folder')

        self.groupBox1 = QGroupBox('Membuat Folder')
        self.label1 = QLabel('Nama Folder yang akan di buat')
        self.newDirEdit = QLineEdit()
        self.createButton = QPushButton('Buat Folder')
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.label1)
        vbox1.addWidget(self.newDirEdit)
        hbox1 = QHBoxLayout()
        hbox1.addStretch()  # mengisi ke kosong an
        hbox1.addWidget(self.createButton)
        hbox1.addStretch()  # mengisi ke kosong an
        vbox1.addLayout(hbox1)
        self.groupBox1.setLayout(vbox1)

        self.groupBox2 = QGroupBox('Mengubah nama Folder')
        self.label2 = QLabel('Nama Folder Lama')
        self.oldDirNameEdit = QLineEdit()
        self.label3 = QLabel('Nama Folder Baru')
        self.newDirNameEdit = QLineEdit()
        self.renameButton = QPushButton('Ubah nama Folder')
        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.label2)
        vbox2.addWidget(self.oldDirNameEdit)
        vbox2.addWidget(self.label3)
        vbox2.addWidget(self.newDirNameEdit)
        hbox2 = QHBoxLayout()
        hbox2.addStretch()
        hbox2.addWidget(self.renameButton)
        hbox2.addStretch()
        vbox2.addLayout(hbox2)
        self.groupBox2.setLayout(vbox2)

        self.groupBox3 = QGroupBox('Menghapus Folder')
        self.label4 = QLabel('Nama Folder yang akan di hapus')
        self.dirNameEdit = QLineEdit()
        self.removeButton = QPushButton('Hapus Folder')
        vbox3 = QVBoxLayout()
        vbox3.addWidget(self.label4)
        vbox3.addWidget(self.dirNameEdit)
        hbox3 = QHBoxLayout()
        hbox3.addStretch()  # mengisi ke kosong an
        hbox3.addWidget(self.removeButton)
        hbox3.addStretch()  # mengisi ke kosong an
        vbox3.addLayout(hbox3)
        self.groupBox3.setLayout(vbox3)

        layout = QVBoxLayout()
        layout.addWidget(self.groupBox1)
        layout.addWidget(self.groupBox2)
        layout.addWidget(self.groupBox3)
        self.setLayout(layout)

        self.createButton.clicked.connect(self.createButtonClick)
        self.renameButton.clicked.connect(self.renameButtonClick)
        self.removeButton.clicked.connect(self.removeButtonClick)


    def createButtonClick(self):
        self.directory = QDir()
        dirName = self.newDirEdit.text()
        if len(self.newDirEdit.text().strip()) == 0:
            QMessageBox.critical(self, 'Kesalahan', 'Nama folder harus di isi')
            self.newDirEdit.setFocus()
            return
        if self.directory.exists(self.newDirEdit.text()):
            QMessageBox.critical(self, 'Kesalahan', 'Nama folder sudah ada')
            self.newDirEdit.setFocus()
            return
        if self.directory.mkdir(dirName):
            QMessageBox.information(self, 'Informasi', 'Nama folder "%s" telah dibuat' % dirName)
        else:
            QMessageBox.information(self, 'Informasi', 'folder gagal di buat')


    def renameButtonClick(self):
        self.directory = QDir()
        if len(self.oldDirNameEdit.text().strip()) == 0:
            QMessageBox.critical(self, 'Kesalahan', 'Nama folder lama harus diisi')
            self.oldDirNameEdit.setFocus()
            return
        if len(self.newDirNameEdit.text().strip()) == 0:
            QMessageBox.critical(self, 'Kesalahan', 'Nama folder baru harus diisi')
            self.newDirNameEdit.setFocus()
            return
        if not self.directory.exists(self.oldDirNameEdit.text()):
            QMessageBox.critical(self, 'Kesalahan', 'Salah kali nama folder nya')
            self.oldDirNameEdit.setFocus()
            return
        oldDirName = self.oldDirNameEdit.text()
        newDirName = self.newDirNameEdit.text()
        if self.directory.rename(oldDirName, newDirName):
            QMessageBox.information(self, 'Informasi', 'Folder "%s" telah diubah menjadi %s' %(oldDirName, newDirName))
        else:
            QMessageBox.information(self, 'Informasi', 'Folder gagal diubah')

    def removeButtonClick(self):
        self.directory = QDir()
        dirName = self.dirNameEdit.text()
        if len(self.dirNameEdit.text().strip()) == 0:
            QMessageBox.critical(self, 'Kesalahan', 'Nama folder harus di isi')
            self.dirNameEdit.setFocus()
            return
        if not self.directory.exists(self.dirNameEdit.text()):
            QMessageBox.critical(self, 'Kesalahan', 'Nama folder Ga ADA')
            self.dirNameEdit.setFocus()
            return
        if self.directory.rmdir(dirName):
            QMessageBox.information(self, 'Informasi', 'Nama folder "%s" telah hapus' % dirName)
        else:
            QMessageBox.information(self, 'Informasi', 'Salah Nama Folder kali')



if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
