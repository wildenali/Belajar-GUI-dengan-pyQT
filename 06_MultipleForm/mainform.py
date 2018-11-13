from PyQt5.QtWidgets import QWidget, QPushButton
from otherform import *

class MainForm(QWidget):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(300, 500)
        self.move(400, 200)
        self.setWindowTitle('Form nya ada DUA')

        self.button = QPushButton('Muncuuuul kan')
        self.button.move(50,50)
        self.button.setParent(self)

        self.button.clicked.connect(self.buttonClick)

    def buttonClick(self):
        self.form = OtherForm()
        self.form.show()
