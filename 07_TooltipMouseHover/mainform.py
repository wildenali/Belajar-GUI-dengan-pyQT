    from PyQt5.QtWidgets import QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont

class MainForm(QWidget):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(300,200)
        self.move(300,300)
        self.setWindowTitle('ToolTip atau Mouse Hover')

        QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('ini adalah <i>TOOLTIP</i> untuk form')

        self.button = QPushButton('keluar')
        self.button.move(50,50)
        self.button.setParent(self)
        self.button.setToolTip('ini TOOLTIP di button')
        self.button.clicked.connect(self.buttonClick)

    def buttonClick(self):
        self.close()
