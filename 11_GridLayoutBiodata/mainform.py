from PyQt5.QtWidgets import (QWidget, QGridLayout, QLabel,
                                QLineEdit, QPushButton)

class MainForm(QWidget):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(400,400)
        self.move(500,100)
        self.setWindowTitle('Grid Layout Biodata')

        self.label1 = QLabel('Nama')
        self.lineEdit1 = QLineEdit()

        self.label2 = QLabel('No Henpong')
        self.lineEdit2 = QLineEdit()

        self.button1 = QPushButton('Cakep')

        layout = QGridLayout()
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)
        layout.addWidget(self.button1, 2, 0, 1, 2)

        self.setLayout(layout)
