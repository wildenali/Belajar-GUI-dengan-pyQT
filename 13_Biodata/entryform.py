from PyQt5.QtWidgets import QDialog, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

class EntryForm(QDialog):
    def __init__(self):
        super(EntryForm, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(300,100)
        self.move(320,280)
        self.setWindowTitle('Isi Biodata')

        self.okButton = QPushButton('Sip')
        self.cancelButton = QPushButton('Ga Jadi')

        hbox = QHBoxLayout()
        hbox.addWidget(self.okButton)
        hbox.addWidget(self.cancelButton)

        self.label1 = QLabel("Nama Lengkap")
        self.nameLineEdit = QLineEdit()
        self.label2 = QLabel("Alamat")
        self.alamatLineEdit = QLineEdit()

        layout = QGridLayout()
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.nameLineEdit, 0, 1)
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.alamatLineEdit, 1, 1)
        layout.addLayout(hbox, 2, 1)
        self.setLayout(layout)

        self.okButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)
