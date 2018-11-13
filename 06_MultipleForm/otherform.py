from PyQt5.QtWidgets import QWidget, QPushButton

class OtherForm(QWidget):
    def __init__(self):
        super(OtherForm, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(200,200)
        self.move(500,100)
        self.setWindowTitle('Form KEDUAAAAAA')

        self.button = QPushButton('keluar')
        self.button.move(50,50)
        self.button.setParent(self)

        self.button.clicked.connect(self.buttonClick)

    def buttonClick(self):
        self.close()
