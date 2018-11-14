from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout

class MainForm(QWidget):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(300,200)
        self.move(300,300)
        self.setWindowTitle('QVerticalLayout')

        self.button1 = QPushButton('Batagor')
        self.button2 = QPushButton('Siomay')
        self.button3 = QPushButton('Martabak')
        self.button4 = QPushButton('Cilok')

        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)

        self.setLayout(layout)
