#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication

class checkMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Siap')

        menubar = self.menuBar()
        viewMenu = menubar.addMenu('View')

        viewStatusAction = QAction('View statusbar', self, checkable=True)
        viewStatusAction.setStatusTip('View statusbar')
        viewStatusAction.setChecked(True)
        viewStatusAction.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatusAction)

        self.setGeometry(500, 300, 300, 200)
        self.setWindowTitle('Cek Menu')
        self.show()

    def toggleMenu(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = checkMenu()
    sys.exit(app.exec_())
