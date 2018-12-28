#!usr/bin/python3
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.statusBar().showMessage('Siap')

        self.setGeometry(300, 300, 250, 150);
        self.setWindowTitle('Status Bar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example();
    sys.exit(app.exec_())
