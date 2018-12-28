#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon

class menu_dan_Toolbar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QAction(QIcon('exit.png'), 'Keluar', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Keluar nih')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Keluar')
        toolbar.addAction(exitAction)

        self.setGeometry(500, 250, 350, 250)
        self.setWindowTitle('Window Utama')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = menu_dan_Toolbar()
    sys.exit(app.exec_())
