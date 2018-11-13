from PyQt5.QtWidgets import QWidget, QPushButton

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(300,200)
        self.move(300,300)
        self.setWindowTitle('button close')

        self.button = QPushButton('TutuT')
        self.button.move(50,50)
        self.button.setParent(self)

        self.button.clicked.connect(self.buttonClick)

    def buttonClick(arg):
        arg.close()
