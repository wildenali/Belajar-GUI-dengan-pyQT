from PyQt5.QtWidgets import QWidget, QLabel

class MinimalForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(300,200)
        self.move(300,500)
        self.setWindowTitle('gui gui sederhana')

        self.label = QLabel('heeey guigui')
        self.label.move(55,40)
        self.label.setParent(self)
