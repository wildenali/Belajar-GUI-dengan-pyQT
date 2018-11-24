#!/usr/bin/python3

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *


class MainForm(QWidget):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(550,450)
        self.move(500,100)
        self.setWindowTitle('MYSQL SQL executor')

        self.label1 = QLabel('Tulis perintah SQL pada kotak di bawah ini')

        self.sqlTextEdit = QTextEdit()

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.label1)
        vbox1.addWidget(self.sqlTextEdit)

        self.emptyLabel = QLabel('')
        self.executeButton = QPushButton('&Eksekusi')

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.emptyLabel)
        vbox2.addWidget(self.executeButton)
        vbox2.addStretch()

        hbox = QHBoxLayout()
        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2)

        self.label2 = QLabel('Hasil query')
        self.tableView = QTableView()
        self.label3 = QLabel('Log')
        self.logList = QListWidget()

        layout = QVBoxLayout()
        layout.addLayout(hbox)
        layout.addWidget(self.label2)
        layout.addWidget(self.tableView)
        layout.addWidget(self.label3)
        layout.addWidget(self.logList)
        self.setLayout(layout)

        self.executeButton.clicked.connect(self.executeButtonClick)

    def executeButtonClick(self):
        specialCommands = ['SHOW', 'DESC', 'DESCRIBE', 'SELECT']
        sql = self.sqlTextEdit.document().toPlainText()

        # memeriksa apakah sql diawali oleh salah satu anggota dari specialCommands atau tidak
        idx = sql.index(' ')
        firstCommand = sql[:idx]
        isSpecialCommand = firstCommand.upper() in specialCommands

        # jika iya
        if isSpecialCommand:
            model = QSqlQueryModel()
            model.setQuery(sql)
            self.tableView.setModel(model)
            self.tableView.show()
        else:
            query = QSqlQuery()
            query.exec_(sql)

        self.logList.addItem(sql)

if __name__ == '__main__':
    a = QApplication(sys.argv)

    db = QSqlDatabase.addDatabase('QMYSQL')
    db.setHostName('localhost')
    db.setDatabaseName('testdb')
    db.setUserName('root')
    db.setPassword('sari')

    if not db.open():
        print('ERROR ', + db.lastError().text())
        sys.exit(1)

    form = MainForm()
    form.show()

    a.exec_()
