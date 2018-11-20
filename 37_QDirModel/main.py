#!/usr/bin/python3

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QWidget):
    def __init__(self):
        super(MainForm, self).__init__()
        self.model = QDirModel()
        self.model.setReadOnly(False)
        self.model.setSorting(QDir.DirsFirst | QDir.IgnoreCase | QDir.Name)
        self.setupUI()

    def setupUI(self):
        self.resize(600,300)
        self.move(300,300)
        self.setWindowTitle('QDirModel')

        self.treeView = QTreeView()
        self.treeView.setModel(self.model)

        # contoh mengaktifkan direktori tertentu
        index = self.model.index('/home/password-sari')

        self.treeView.expand(index)
        self.treeView.scrollTo(index)
        self.treeView.setCurrentIndex(index)
        self.treeView.resizeColumnToContents(0)

        self.createButton = QPushButton('Buat Folder')
        self.deleteButton = QPushButton('Hapus')
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.createButton)
        hbox.addWidget(self.deleteButton)

        layout = QVBoxLayout()
        layout.addWidget(self.treeView)
        layout.addLayout(hbox)
        self.setLayout(layout)

        self.createButton.clicked.connect(self.createButtonClick)
        self.deleteButton.clicked.connect(self.deleteButtonClick)

    def createButtonClick(self):
        index = self.treeView.currentIndex()
        if not index.isValid(): return

        dialogResult = QInputDialog.getText(self, "Membuat Folder", "Masukan nama Folder yang akan di buat: ")
        newDirName = dialogResult[0]

        if len(newDirName) == 0: return

        self.model.mkdir(index, newDirName)

    def deleteButtonClick(self):
        index = self.treeView.currentIndex()
        if not index.isValid(): return

        if (self.model.fileInfo(index).isDir()):
            # Menghapus folder
            self.model.rmdir(index)
        else:
            self.model.remove(index)


if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
