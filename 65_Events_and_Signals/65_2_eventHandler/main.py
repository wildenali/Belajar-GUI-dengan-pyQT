#!/usr/bin/python3

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

class evenHandler(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(500, 250, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Space:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = evenHandler()
    sys.exit(app.exec_())
