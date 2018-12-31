#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QApplication

class lineEdit(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.label = QLabel(self)
        self.label.move(60, 40)

        lineEdit = QLineEdit(self)
        lineEdit.move(60, 100)

        lineEdit.textChanged[str].connect(self.onChanged)

        self.setGeometry(500, 300, 280, 170)
        self.setWindowTitle("QLineEdit")
        self.show()

    def onChanged(self, text):
        self.label.setText(text)
        self.label.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = lineEdit()
    sys.exit(app.exec_())
