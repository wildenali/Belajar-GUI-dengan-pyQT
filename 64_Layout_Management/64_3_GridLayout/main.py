#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication

class gridLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Back', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+',]

        position = [(i,j) for i in range(5) for j in range(4)]

        for position, name in zip(position, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(500, 250)
        self.setWindowTitle('Calculator')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainForm = gridLayout()
    sys.exit(app.exec_())
