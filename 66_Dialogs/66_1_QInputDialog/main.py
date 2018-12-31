#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication

class inputDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.button = QPushButton('Dialog', self)
        self.button.move(20, 20)
        self.button.clicked.connect(self.showDialog)

        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(130, 22)

        self.setGeometry(500, 250, 290, 150)
        self.setWindowTitle('Input Dialog')
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Entrr your name:')

        if ok:
            self.lineEdit.setText(str(text))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = inputDialog()

    sys.exit(app.exec_())
