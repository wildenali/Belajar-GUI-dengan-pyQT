from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class MainForm(QWidget):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(250,250)
        self.move(300,300)
        self.setWindowTitle('Kalkulator')

        self.lineEdit = QLineEdit()
        self.lineEdit.setAlignment(Qt.AlignRight)
        self.lineEdit.setFont(QFont('SansSerif',14))
        self.lineEdit.setDisabled(True)

        self._7Button = QPushButton('7')
        self._8Button = QPushButton('8')
        self._9Button = QPushButton('9')
        self.divButton = QPushButton('/')
        self.clearButton = QPushButton('clear')
        self._4Button = QPushButton('4')
        self._5Button = QPushButton('5')
        self._6Button = QPushButton('6')
        self.mulButton = QPushButton('x')
        self._1Button = QPushButton('1')
        self._2Button = QPushButton('2')
        self._3Button = QPushButton('3')
        self.minusButton = QPushButton('-')
        self._0Button = QPushButton('0')
        self.dotButton = QPushButton('.')
        self.percentageButton = QPushButton('%')
        self.plusButton = QPushButton('+')
        self.calculateButton = QPushButton("=")

        layout = QGridLayout()
        layout.addWidget(self.lineEdit, 0, 0, 1, 4)
        layout.addWidget(self._7Button, 1, 0)
        layout.addWidget(self._8Button, 1, 1)
        layout.addWidget(self._9Button, 1, 2)
        layout.addWidget(self.clearButton, 1, 3)
        layout.addWidget(self._4Button, 2, 0)
        layout.addWidget(self._5Button, 2, 1)
        layout.addWidget(self._6Button, 2, 2)
        layout.addWidget(self.mulButton, 2, 3)
        layout.addWidget(self._1Button, 3, 0)
        layout.addWidget(self._2Button, 3, 1)
        layout.addWidget(self._3Button, 3, 2)
        layout.addWidget(self.divButton, 3, 3)
        layout.addWidget(self._0Button, 4, 0)
        layout.addWidget(self.dotButton, 4, 1)
        layout.addWidget(self.minusButton, 4, 2)
        layout.addWidget(self.plusButton, 4, 3)
        layout.addWidget(self.percentageButton, 5, 0)
        layout.addWidget(self.calculateButton, 5, 1, 1, 3)
        self.setLayout(layout)

        self._0Button.clicked.connect(lambda: self.writeDigit(0))
        self._1Button.clicked.connect(lambda: self.writeDigit(1))
        self._2Button.clicked.connect(lambda: self.writeDigit(2))
        self._3Button.clicked.connect(lambda: self.writeDigit(3))
        self._4Button.clicked.connect(lambda: self.writeDigit(4))
        self._5Button.clicked.connect(lambda: self.writeDigit(5))
        self._6Button.clicked.connect(lambda: self.writeDigit(6))
        self._7Button.clicked.connect(lambda: self.writeDigit(7))
        self._8Button.clicked.connect(lambda: self.writeDigit(8))
        self._9Button.clicked.connect(lambda: self.writeDigit(9))
        self.mulButton.clicked.connect(lambda: self.writeOperator('*'))
        self.divButton.clicked.connect(lambda: self.writeOperator('/'))
        self.plusButton.clicked.connect(lambda: self.writeOperator('+'))
        self.minusButton.clicked.connect(lambda: self.writeOperator('-'))
        self.dotButton.clicked.connect(self.writePoint)
        self.clearButton.clicked.connect(self.lineEdit.clear)
        self.calculateButton.clicked.connect(self.calculateButtonClick)
        self.percentageButton.clicked.connect(self.percentageButtonClick)

    def writeDigit(self, digit):
        if digit in range(0, 10):
            self.lineEdit.setText(self.lineEdit.text() + str(digit))

    def writeOperator(self, operator):
        if len(self.lineEdit.text()) == 0: return
        if operator in ['*','/','+','-']:
            if self.lineEdit.text()[-1] in ['*','/','+','-']:
                self.lineEdit.setText(self.lineEdit.text()[:-1] + operator)
            else:
                self.lineEdit.setText(self.lineEdit.text() + operator)

    def writePoint(self):
        if len(self.lineEdit.text()) == 0 or self.lineEdit.text()[-1] in ['*','/','+','-']:
            return
        self.lineEdit.setText(self.lineEdit.text() + '.')


    def calculateButtonClick(self):
        expression = self.lineEdit.text()
        if len(expression) == 0:
            return
        try:
            result = eval(expression)
            self.lineEdit.setText(str(result))
        except:
            self.lineEdit.setText('Erour Coy')

    def percentageButtonClick(self):
        expression = self.lineEdit.text()
        if len(expression) == 0:
            return
        try:
            result = eval(expression) / 100
            self.lineEdit.setText(str(result))
        except:
            self.lineEdit.setText('EROOOOR')
