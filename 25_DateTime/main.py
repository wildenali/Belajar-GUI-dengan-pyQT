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
        self.resize(500,200)
        self.move(300,300)
        self.setWindowTitle('Date and Time')

        self.dateLabel = QLabel('Tanggal')
        self.dateEdit = QDateEdit()
        self.dateEdit.setDisplayFormat('dddd dd/MM/yyyy')
        self.dateEdit.setDate(QDate.currentDate())

        self.timeLabel = QLabel('Waktu')
        self.timeEdit = QTimeEdit()
        self.timeEdit.setDisplayFormat('hh:mm')
        self.timeEdit.setTime(QTime.currentTime())

        self.dateTimeLabel = QLabel('Tanggal dan Waktu')
        self.dateTimeEdit = QDateTimeEdit()
        self.dateTimeEdit.setDisplayFormat('dddd dd/MM/yyyy hh:mm')
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())

        self.okButton = QPushButton('&Sip')
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.okButton)

        layout = QGridLayout()
        layout.addWidget(self.dateLabel, 0, 0)
        layout.addWidget(self.dateEdit, 0, 1)
        layout.addWidget(self.timeLabel, 1, 0)
        layout.addWidget(self.timeEdit, 1, 1)
        layout.addWidget(self.dateTimeLabel, 2, 0)
        layout.addWidget(self.dateTimeEdit, 2, 1)
        layout.addLayout(hbox, 3, 0, 1, 2)
        self.setLayout(layout)

        self.okButton.clicked.connect(self.okButtonClick)

    def okButtonClick(self):
        QMessageBox.information(self, 'Informasi',
            'Date: ' + self.dateEdit.date().toString() + '\n' +
            'Time: ' + self.timeEdit.time().toString() + '\n' +
            'DateTime: ' + self.dateTimeEdit.dateTime().toString() + '\n')


if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
