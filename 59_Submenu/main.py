#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication

class subMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        importMenu = QMenu('Import', self)
        importMailAction = QAction('Import mail', self)
        importMenu.addAction(importMailAction)

        newAct = QAction('New', self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(importMenu)

        self.setGeometry(500, 300, 300, 200)
        self.setWindowTitle('Submenu')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = subMenu()
    sys.exit(app.exec_())
