from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton

class MainForm(QWidget):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(300,200)
        self.move(400,200)
        self.setWindowTitle('Clear si Line Edit')

        self.lineEdit = QLineEdit()
        self.lineEdit.setText('Hapus ini dong')

        self.button1 = QPushButton('Bersihkaan')
        self.button2 = QPushButton('Tutut')

        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)

        layout = QVBoxLayout()
        layout.addWidget(self.lineEdit)
        layout.addLayout(hbox)
        self.setLayout(layout)

        self.button1.clicked.connect(self.lineEdit.clear)
        self.button2.clicked.connect(self.close)
