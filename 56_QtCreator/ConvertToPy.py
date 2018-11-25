# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '05_ConvertToPy.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 90, 111, 17))
        self.label.setObjectName("label")
        self.nameEdit = QtWidgets.QLineEdit(Dialog)
        self.nameEdit.setGeometry(QtCore.QRect(70, 120, 231, 27))
        self.nameEdit.setObjectName("nameEdit")
        self.helloButton = QtWidgets.QPushButton(Dialog)
        self.helloButton.setGeometry(QtCore.QRect(40, 160, 99, 27))
        self.helloButton.setObjectName("helloButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 180, 99, 27))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        self.pushButton_2.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Masukan Nama"))
        self.helloButton.setText(_translate("Dialog", "Hallo"))
        self.pushButton_2.setText(_translate("Dialog", "Keluar"))

