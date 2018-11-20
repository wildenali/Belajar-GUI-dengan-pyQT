#!/usr/bin/python3

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class AddForm(QDialog):
    def __init__(self):
        super(AddForm, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(350,130)
        self.move(400,400)
        self.setWindowTitle('Tambah Data')

        self.label1 = QLabel('Bahasa Pemrograman')
        self.languageEdit = QLineEdit()
        self.label2 = QLabel('Nama Penciptanya')
        self.nameEdit = QLineEdit()

        grid = QGridLayout()
        grid.addWidget(self.label1, 0, 0)
        grid.addWidget(self.languageEdit, 0, 1)
        grid.addWidget(self.label2, 1, 0)
        grid.addWidget(self.nameEdit, 1, 1)

        self.okButton = QPushButton('Ok Sip')
        self.cancelButton =QPushButton('Ga Jadi Ah')

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.okButton)
        hbox.addWidget(self.cancelButton)

        layout = QVBoxLayout()
        layout.addLayout(grid)
        layout.addLayout(hbox)
        self.setLayout(layout)

        self.okButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)

class MainForm(QWidget):
    lastRecordNumber = -1
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(450,300)
        self.move(300,200)
        self.setWindowTitle('QDialog.accept dan QDialog.reject')

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(0)
        self.setColumnAndHeaders()

        self.addButton = QPushButton('Tambah')
        self.deleteButton = QPushButton('Hapus')
        self.exitButton = QPushButton('Keluar')

        vbox = QVBoxLayout()
        vbox.addWidget(self.addButton)
        vbox.addWidget(self.deleteButton)
        vbox.addStretch()
        vbox.addWidget(self.exitButton)

        layout = QHBoxLayout()
        layout.addWidget(self.tableWidget)
        layout.addLayout(vbox)
        self.setLayout(layout)

        self.addButton.clicked.connect(self.addButtonClick)
        self.deleteButton.clicked.connect(self.deleteButtonClick)
        self.exitButton.clicked.connect(self.exitButtonClick)

    def setColumnAndHeaders(self):
        self.tableWidget.setColumnCount(2)
        columnHeaders = ['Bahasa Pemrograman', 'Nama Pencipta']
        self.tableWidget.setHorizontalHeaderLabels(columnHeaders)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setStretchLastSection(True)

    def addRow(self, row, itemLabels=[]):
        for i in range(2):
            item = QTableWidgetItem()
            item.setText(itemLabels[i])
            self.tableWidget.setItem(row, i, item)

    def addButtonClick(self):
        if MainForm.lastRecordNumber == self.tableWidget.rowCount()-1:
            self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
        form = AddForm()
        if form.exec_() == QDialog.Accepted:
            MainForm.lastRecordNumber += 1
            language = form.languageEdit.text()
            name = form.nameEdit.text()
            data = [language, name]
            self.addRow(MainForm.lastRecordNumber, data)

    def deleteButtonClick(self):
        tableData = []
        for i in range(0, self.tableWidget.rowCount()):
            language = self.tableWidget.item(i, 0).text()
            name = self.tableWidget.item(i, 1).text()
            tableData.append([language, name])

        row = self.tableWidget.currentRow()
        del tableData[row]

        MainForm.lastRecordNumber -= 1
        self.tableWidget.clear()
        self.setColumnAndHeaders()
        self.tableWidget.setRowCount(len(tableData))
        for i in range(0, len(tableData)):
            data = tableData[i]
            self.addRow(i, data)

    def exitButtonClick(self):
        self.close()

if __name__ == '__main__':
    a =  QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
