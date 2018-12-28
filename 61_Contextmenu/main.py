#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QMainWindow, qApp, QMenu, QApplication

class contextMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(500, 300, 300, 200)
        self.setWindowTitle('Context menu')
        self.show()

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        newAction = cmenu.addAction("New")
        openAction = cmenu.addAction("Open")
        quitAction = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAction:
            qApp.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = contextMenu()
    sys.exit(app.exec_())
