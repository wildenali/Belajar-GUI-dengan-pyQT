#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class menuSederhana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        exitAct = QAction(QIcon('exit.jpeg'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Keluar nih ?')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.setGeometry(500, 200, 400, 200)
        self.setWindowTitle('Menu Sederhana')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = menuSederhana()
    sys.exit(app.exec_())
