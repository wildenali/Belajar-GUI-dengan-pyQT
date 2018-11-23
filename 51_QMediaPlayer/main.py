#!/usr/bin/python3

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *

class MainForm(QWidget):
    def __init__(self):
        super(MainForm, self).__init__()
        self.player = QMediaPlayer(self)
        self.setupUI()

    def setupUI(self):
        self.resize(500,450)
        self.move(500,100)
        self.setWindowTitle('Play musiiiiik')

        self.label1 = QLabel('Progress')
        self.progressSlider = QSlider(Qt.Horizontal)
        self.label2 = QLabel('Volume')
        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.setValue(100)

        grid = QGridLayout()
        grid.addWidget(self.label1, 0, 0)
        grid.addWidget(self.progressSlider, 0, 1)
        grid.addWidget(self.label2, 1, 0)
        grid.addWidget(self.volumeSlider, 1, 1)

        self.openButton = QPushButton('Open')
        self.playButton = QPushButton('Play')
        self.pauseButton = QPushButton('Pause')
        self.stopButton = QPushButton('Stop')

        hbox = QHBoxLayout()
        hbox.addWidget(self.openButton)
        hbox.addWidget(self.playButton)
        hbox.addWidget(self.pauseButton)
        hbox.addWidget(self.stopButton)
        hbox.addStretch()

        layout = QVBoxLayout()
        layout.addLayout(grid)
        layout.addLayout(hbox)
        self.setLayout(layout)

        self.openButton.clicked.connect(self.openButtonClick)
        self.playButton.clicked.connect(self.playButtonClick)
        self.pauseButton.clicked.connect(self.pauseButtonClick)
        self.stopButton.clicked.connect(self.stopButtonClick)

        self.progressSlider.sliderMoved.connect(self.progressSliderMoved)
        self.volumeSlider.sliderMoved.connect(self.volumeSliderMoved)
        self.player.positionChanged.connect(self.playerPositionChanged)
        self.player.durationChanged.connect(self.playerDurationChanged)

    def openButtonClick(self):
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile('/home/password-sari/Documents/wildenali github/Belajar-GUI-dengan-pyQT/51_QMediaPlayer/gameofthrones_soundtrack.mp3')))

    def playButtonClick(self):
        self.player.play()

    def pauseButtonClick(self):
        self.player.pause()

    def stopButtonClick(self):
        self.player.stop()

    def progressSliderMoved(self):
        self.player.setPosition(self.progressSlider.value())

    def volumeSliderMoved(self):
        self.player.setVolume(self.volumeSlider.value())

    def playerPositionChanged(self, position):
        self.progressSlider.setValue(position)

    def playerDurationChanged(self, position):
        self.progressSlider.setMaximum(position)

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
