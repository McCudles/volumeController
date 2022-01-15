import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import time
from threading import *
import threadWithTrace as twt
import main

# window and button stuff
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.ChangeColorTestButton()
        self.PlayPauseButton()
        self.setupUI()

    def setupUI(self):
        self.setObjectName("Dialog")
        self.resize(800, 400)
        self.setMinimumSize(QtCore.QSize(800, 400))
        self.setMaximumSize(QtCore.QSize(800, 400))

    play = False

    def UpdateButtonStyle(self):
        print(main.query())
        self.playPauseButton.setStyleSheet("background-color: %s" % main.query()[2][2])

    def ChangeColorTestButton(self):
        self.changeColorTestButton = QPushButton("Change color lol", self)
        self.changeColorTestButton.clicked.connect(self.UpdateButtonStyle)
        self.changeColorTestButton.move(40, 90)

    def PlayPauseButton(self):
        self.playPauseButton = QPushButton("Click Me", self)
        self.playPauseButton.resize(200, 70)
        self.playPauseButton.move(40, 10)
        self.playPauseButton.setCheckable(True)
        self.playPauseButton.clicked.connect(self.ButtonLogic)
        self.SetButtonStyle()
        # self.setGeometry(0, 0, 1000, 300)
        self.show()

    def runVolumeController(self):
        main.restartTime()
        main.run()

    def ButtonLogic(self):
        if self.play:  # pausing
            self.play = not self.play
            self.volumeThread.kill()
            self.volumeThread.join()
            self.SetButtonStyle()

        else:  # start playing
            self.play = not self.play
            self.volumeThread = twt.thread_with_trace(target=self.runVolumeController)
            self.volumeThread.start()
            self.SetButtonStyle()

    def SetButtonStyle(self):
        if self.play:
            self.playPauseButton.setStyleSheet("background-color: lightgreen")
            self.playPauseButton.setText("  Playing")
            self.playPauseButton.setToolTip("Now playing the Volume Controller")
            self.playPauseButton.setIcon(QIcon("./images/pause.png"))

        else:
            self.playPauseButton.setStyleSheet("background-color: lightblue")
            self.playPauseButton.setText("  Paused")
            self.playPauseButton.setToolTip("No longer playing the Volume Controller")
            self.playPauseButton.setIcon(QIcon("./images/play.png"))

    def ButtonAction(self):
        self.play = not (self.play)
        print(self.play)
        self.SetButtonStyle(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
