#!/usr/bin/python3

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QWidget):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.resize(800,400)
        self.move(300,100)
        self.setWindowTitle('Tree Widget Phone Book')

        self.tree = QTreeWidget()
        self.tree.setColumnCount(3)
        columnHeaders = ['Judul Buku', 'Penulis', 'Penerbit']
        self.tree.setHeaderLabels(columnHeaders)

        parent1 = self.addTopLevel('Python')
        self.addChild(parent1, 'Python 3 Object Oriented Programming', 'Dusty Philips', 'PACKT Publishing')
        self.addChild(parent1, 'Numerical Python', 'Robert Johansson', 'Apress')
        self.addChild(parent1, 'A Primer Scientific Programming with Python', 'Hans Peter Langtangen', 'Springer')

        parent2 = self.addTopLevel('Ruby')
        self.addChild(parent2, 'Beginning Ruby', 'Peter Cooper', 'Apress')
        self.addChild(parent2, 'Ruby Under a Microscope', 'Pat Shaughnessy', 'No Starch Press')

        self.lineEdit = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.tree)
        layout.addWidget(self.lineEdit)
        self.setLayout(layout)

        self.tree.itemClicked.connect(self.treeItemClick)

    def treeItemClick(self):
        item  = self.tree.currentItem()
        self.lineEdit.setText(item.text(0))

    def addTopLevel(self, category):
        item = QTreeWidgetItem()
        item.setText(0, category)
        self.tree.addTopLevelItem(item)
        return item

    def addChild(self, parent, title, author, publisher):
        item = QTreeWidgetItem(parent)
        item.setText(0, title)
        item.setText(1, author)
        item.setText(2, publisher)
        parent.addChild(item)
        return item

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
