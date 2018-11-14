from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout

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

        layout = QGridLayout()
        layout.addWidget(self.button1, 0, 0)
        layout.addWidget(self.button2, 0, 1)
        layout.addWidget(self.button3, 1, 0)
        layout.addWidget(self.button4, 1, 1)

        self.setLayout(layout)
