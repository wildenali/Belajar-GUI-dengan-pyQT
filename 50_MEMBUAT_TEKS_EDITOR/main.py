#!/usr/bin/python3

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

PROGRAM_NAME='Wilden Editor'

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.currentFileName = ''
        self.setupUI()

    def setupUI(self):
        self.resize(500,450)
        self.move(500,100)
        self.setWindowTitle(PROGRAM_NAME + ' - Untitled')

        # inisialisasi teks pada statusbar
        self.statusBar().showMessage('Ketikan teks yang Anda inginkan')

        # mendapatkan objek menubar
        menubar = self.menuBar()

        # membuat menu File dan menempatkannya ke dalam menuBar
        fileMenu = menubar.addMenu('&File')

        # membuat aksi untuk menu File
        fileNewAction = QAction(QIcon('icons/new.png'), '&New', self)
        fileNewAction.setShortcut('Ctrl+N')
        fileNewAction.setStatusTip('Buat teks baru')
        fileNewAction.triggered.connect(self.fileNewActionTriggered)
        fileMenu.addAction(fileNewAction)

        fileOpenACtion = QAction(QIcon('icons/open.png'), '&Open', self)
        fileOpenACtion.setShortcut('Ctrl+O')
        fileOpenACtion.setStatusTip('Buka File')
        fileOpenACtion.triggered.connect(self.fileOpenACtionTriggered)
        fileMenu.addAction(fileOpenACtion)

        fileMenu.addSeparator()

        fileSaveAction = QAction(QIcon('icons/save.png'), '&Save', self)
        fileSaveAction.setShortcut('Ctrl+S')
        fileSaveAction.setStatusTip('Save File')
        fileSaveAction.triggered.connect(self.fileSaveActionTriggered)
        fileMenu.addAction(fileSaveAction)

        fileSaveAsAction = QAction(QIcon('none'), 'Save &As...', self)
        fileSaveAsAction.setStatusTip('Simpan teks ke file lain')
        fileSaveAsAction.triggered.connect(self.fileSaveAsActionTriggered)
        fileMenu.addAction(fileSaveAsAction)
        fileMenu.addSeparator()

        fileExitAction = QAction(QIcon('icons/exit.png'), '&Exit', self)
        fileExitAction.setShortcut('Ctrl+Q')
        fileExitAction.setStatusTip('Buat document baru')
        fileExitAction.triggered.connect(self.fileExitActionTriggered)
        fileMenu.addAction(fileExitAction)

        # membuat menu Edit dan menempatkannya ke dalam menubar
        editMenu = menubar.addMenu('&Edit')

        # Membuat aksi untuk menu Edit
        editCutAction = QAction(QIcon('icons/cut.png'), '&Cut', self)
        editCutAction.setShortcut('Ctrl+X')
        editCutAction.setStatusTip('Potong Teks')
        editCutAction.triggered.connect(self.editCutActionTriggered)
        editMenu.addAction(editCutAction)

        editCopyAction = QAction(QIcon('icons/copy.png'), '&Copy', self)
        editCopyAction.setShortcut('Ctrl+C')
        editCopyAction.setStatusTip('Salin Teks')
        editCopyAction.triggered.connect(self.editCopyActionTriggered)
        editMenu.addAction(editCopyAction)

        editMenu.addSeparator()

        editPasteAction = QAction(QIcon('icons/paste.png'), '&Paste', self)
        editPasteAction.setShortcut('Ctrl+V')
        editPasteAction.setStatusTip('Tempel Teks')
        editPasteAction.triggered.connect(self.editPasteActionTriggered)
        editMenu.addAction(editPasteAction)

        # membuat menu Foormat dan menempatkannya ke dalam menubar
        formatMenu = menubar.addMenu('&Format')

        # membuat aksi untuk menu Format
        formatFontAction = QAction(QIcon(None), '&Font...', self)
        formatFontAction.setStatusTip('Menentukan jenis dan ukuran huruf pada teks yang disorot')
        formatFontAction.triggered.connect(self.formatFontActionTriggered)
        formatMenu.addAction(formatFontAction)

        # membuat toolbar
        toolbar = self.addToolBar('')
        toolbar.addAction(fileNewAction)
        toolbar.addAction(fileOpenACtion)
        toolbar.addAction(fileSaveAction)
        toolbar.addSeparator()
        toolbar.addAction(editCutAction)
        toolbar.addAction(editCopyAction)
        toolbar.addAction(editPasteAction)

        # membuat objek QTextEdit dan menempatkannya ke dela pusat widget
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

    def confirmation(self):
        if self.textEdit.document().isModified():
            response = QMessageBox.question(self, 'Konfirmasi', 'Tejs telah dimodifikasi. Simpan?')
            if response == QMessageBox.Yes:
                self.fileSaveActionTriggered()

    def fileNewActionTriggered(self):
        self.confirmation()
        self.textEdit.document().clear()
        self.currentFileName = ''
        self.setWindowTitle(PROGRAM_NAME + ' - Untitled')

    def fileOpenACtionTriggered(self):
        import os
        self.confirmation()
        fileName = QFileDialog.getOpenFileName(self, 'Pilih File', os.curdir, 'File Teks (*.txt)', '*.txt')
        if not fileName[0]: return
        self.currentFileName = fileName[0]
        self.setWindowTitle(PROGRAM_NAME + ' - ' + self.currentFileName)
        fileHandle = QFile(fileName[0])
        if not fileHandle.open(QIODevice.ReadOnly): return
        stream = QTextStream(fileHandle)
        self.textEdit.setPlainText(stream.readAll())
        fileHandle.close()

    def writeToFile(self):
        fileHandle = QFile(self.currentFileName)
        if not fileHandle.open(QIODevice.WriteOnly): return
        stream = QTextStream(fileHandle)
        stream << self.textEdit.document().toPlainText()
        stream.flush()
        fileHandle.close()
        self.textEdit.document().setModified(False)

    def fileSaveActionTriggered(self):
        if self.currentFileName == '':
            # Mengeksekusi aksi Save AS
            self.fileSaveAsActionTriggered()
        else:
            self.writeToFile()

    def fileSaveAsActionTriggered(self):
        import os
        fileName = QFileDialog.getSaveFileName(self, 'Simpan File', os.curdir, 'File Text (*.txt)', '*.txt')
        if not fileName[0]: return
        self.currentFileName = fileName[0]
        self.setWindowTitle(PROGRAM_NAME + ' - ' + self.currentFileName)
        self.writeToFile()

    def fileExitActionTriggered(self):
        sys.exit(0)

    def editCutActionTriggered(self):
        self.textEdit.cut()

    def editCopyActionTriggered(self):
        self.textEdit.copy()

    def editPasteActionTriggered(self):
        self.textEdit.paste()

    def formatFontActionTriggered(self):
        fontTuple = QFontDialog.getFont(QFont('Sans Serif', 11), self, 'Pilih Font')
        if fontTuple[0]:
            self.textEdit.setCurrentFont(fontTuple[0])

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
