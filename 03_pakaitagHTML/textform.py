from PyQt5.QtWidgets import QWidget, QLabel

class TextForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(500,500)
        self.move(300, 200)
        self.setWindowTitle('pakai tag HTML')

        self.label1 = QLabel('<h1> Hello <font color = red>batagor</font>, dibeli</h1> ')
        self.label1.move(10,10)
        self.label1.setParent(self)

        self.label2 = QLabel('''Teks ini di buat dengan tag HTML,<br>
                                <b>tebel nih</b>,<br>
                                <i>miring nih</i>,<br>
                                <u>garis bawah nih</u><br>''')
        self.label2.setWordWrap(True)
        self.label2.move(10,50)
        self.label2.setParent(self)
