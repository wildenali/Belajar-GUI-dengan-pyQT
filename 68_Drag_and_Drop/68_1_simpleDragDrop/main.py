#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QLineEdit, QApplication

class tombol(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText(e.mimeData().text())

class dragNdrop(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = QPushButton("Tombol", self)
        button.move(190, 65)

        self.setWindowTitle('Simple drag n drop')
        self.setGeometry(500, 300, 300, 150)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = dragNdrop()
    ex.show()
    app.exec_()
