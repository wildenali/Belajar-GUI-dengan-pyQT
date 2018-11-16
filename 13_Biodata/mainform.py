from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLineEdit,
                                QPushButton, QListWidget)

from entryform import *

class MainForm(QWidget):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(500,300)
        self.move(500,200)
        self.setWindowTitle('Biodata')

        self.addButton = QPushButton('Tambah')
        self.editButton = QPushButton('Ubah')
        self.deleteButton = QPushButton('Haapus')
        self.clearButton = QPushButton('Kosongkan')
        self.exitButton = QPushButton('Keluar')

        hbox = QHBoxLayout()
        hbox.addWidget(self.addButton)
        hbox.addWidget(self.editButton)
        hbox.addWidget(self.deleteButton)
        hbox.addWidget(self.clearButton)
        hbox.addWidget(self.exitButton)

        self.contactList = QListWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.contactList)
        layout.addLayout(hbox)
        self.setLayout(layout)

        self.addButton.clicked.connect(self.addButtonClick)
        self.editButton.clicked.connect(self.editButtonClick)
        self.deleteButton.clicked.connect(self.deleteButtonClick)
        self.clearButton.clicked.connect(self.contactList.clear)
        self.exitButton.clicked.connect(self.close)

    def addButtonClick(self):
        self.entryForm = EntryForm()
        if self.entryForm.exec_() == QDialog.Accepted:
            self.contactList.addItem(self.entryForm.nameLineEdit.text() + ' - ' + self.entryForm.alamatLineEdit.text())

    def editButtonClick(self):
        if self.contactList.currentRow() < 0: return
        self.entryForm = EntryForm()
        s = str(self.contactList.currentItem().text())
        idx = s.index('-')
        self.entryForm.nameLineEdit.setText(s[:(idx-1)])
        self.entryForm.alamatLineEdit.setText(s[(idx+2):])

        if self.entryForm.exec_() == QDialog.Accepted:
            self.contactList.currentItem().setText(self.entryForm.nameLineEdit.text() + ' - ' + self.entryForm.alamatLineEdit.text())

    def deleteButtonClick(self):
        row = self.contactList.currentRow()
        if row >= 0:
            self.contactList.takeItem(row)
