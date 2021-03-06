from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import time
from threading import *
import threadWithTrace as twt
import main
import volumeController


class Ui_Dialog(object):
    def __init__(self):
        self.play = False

        # setting window size BG color
        Dialog.setObjectName("Window")
        Dialog.resize(800, 400)
        Dialog.setMinimumSize(QtCore.QSize(800, 400))
        Dialog.setMaximumSize(QtCore.QSize(800, 400))
        font = QtGui.QFont()
        font.setPointSize(8)
        Dialog.setFont(font)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet(
            "background-color: rgb(54, 52, 53);\n" "selection-color: rgb(28, 39, 255);"
        )

        # spawning progress bar
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 360, 781, 31))
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet("color: rgb(255, 255, 255);")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        # spawning play button
        self.playButton = QtWidgets.QPushButton(Dialog)
        self.playButton.setGeometry(QtCore.QRect(10, 110, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.playButton.setFont(font)
        self.playButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.playButton.setStyleSheet(
            "background-color: rgb(6, 176, 37);\n" "\n" 'font: 36pt "Dubai";'
        )
        self.playButton.setObjectName("playButton")
        self.playButton.clicked.connect(self.playButtonLogic)

        # spawning reset button
        self.resetButton = QtWidgets.QPushButton(Dialog)
        self.resetButton.setGeometry(QtCore.QRect(10, 180, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.resetButton.setFont(font)
        self.resetButton.setAutoFillBackground(False)
        self.resetButton.setStyleSheet(
            "\n"
            'font: 36pt "Dubai";\n'
            "color: rgb(230, 230, 230);\n"
            "background-color: rgb(117, 117, 117);"
        )
        self.resetButton.setObjectName("resetButton")
        self.resetButton.clicked.connect(self.resetButtonLogic)

        # spawning logo image
        self.logo = QtWidgets.QLabel(Dialog)
        self.logo.setGeometry(QtCore.QRect(0, -10, 271, 141))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setAutoFillBackground(False)
        self.logo.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("./images/biglogowhite.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("label")

        # spawning LCD timer
        self.lcdTimer = QtWidgets.QLCDNumber(Dialog)
        self.lcdTimer.setGeometry(QtCore.QRect(10, 250, 361, 101))
        self.lcdTimer.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.lcdTimer.setObjectName("lcdNumber")

        # spawning box that shows the color of the round currently in
        self.roundIndicatorColor = QtWidgets.QGraphicsView(Dialog)
        self.roundIndicatorColor.setGeometry(QtCore.QRect(660, 10, 91, 81))
        self.roundIndicatorColor.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.roundIndicatorColor.setObjectName("roundIndicatorColor")

        # spawning directions text
        self.directionsText = QtWidgets.QLabel(Dialog)
        self.directionsText.setGeometry(QtCore.QRect(290, 20, 181, 61))
        self.directionsText.setAutoFillBackground(False)
        self.directionsText.setWordWrap(True)
        self.directionsText.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "background-color: rgba(255, 255, 255, 0);\n"
            'font: 8pt "MS PGothic";\n'
            'font: 8pt "MS Shell Dlg 2";'
        )
        self.directionsText.setObjectName("directionsText")

        # spawning the makeGraph.py resulting image
        self.graph = QtWidgets.QLabel(Dialog)
        self.graph.setGeometry(QtCore.QRect(400, 110, 351, 171))
        self.graph.setText("")
        self.graph.setPixmap(QtGui.QPixmap("./images/figure.png"))
        self.graph.setScaledContents(True)
        self.graph.setObjectName("label_3")

        # spawning green horizontal slider
        self.greenSlider = QtWidgets.QSlider(Dialog)
        self.greenSlider.setGeometry(QtCore.QRect(420, 110, 22, 171))
        self.greenSlider.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.greenSlider.setOrientation(QtCore.Qt.Vertical)
        self.greenSlider.setObjectName("verticalSlider")

        # spawning yellow horizontal slider
        self.yellowSlider = QtWidgets.QSlider(Dialog)
        self.yellowSlider.setGeometry(QtCore.QRect(600, 110, 22, 171))
        self.yellowSlider.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.yellowSlider.setOrientation(QtCore.Qt.Vertical)
        self.yellowSlider.setObjectName("verticalSlider_2")

        # spawning red horizontal slider
        self.redSlider = QtWidgets.QSlider(Dialog)
        self.redSlider.setGeometry(QtCore.QRect(670, 110, 22, 171))
        self.redSlider.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.redSlider.setOrientation(QtCore.Qt.Vertical)
        self.redSlider.setObjectName("verticalSlider_3")
        # spawning text that says "Green Bell/ Start of Round"
        self.greenSliderText = QtWidgets.QLabel(Dialog)
        self.greenSliderText.setGeometry(QtCore.QRect(380, 280, 121, 71))
        self.greenSliderText.setAutoFillBackground(False)
        self.greenSliderText.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "background-color: rgba(255, 255, 255, 0);\n"
            'font: 8pt "MS PGothic";\n'
            'font: 16pt "MS Shell Dlg 2";'
        )
        self.greenSliderText.setWordWrap(True)
        self.greenSliderText.setObjectName("label_4")

        # spawning text that says "Yellow Bell"
        self.yellowSliderText = QtWidgets.QLabel(Dialog)
        self.yellowSliderText.setGeometry(QtCore.QRect(580, 280, 71, 61))
        self.yellowSliderText.setAutoFillBackground(False)
        self.yellowSliderText.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "background-color: rgba(255, 255, 255, 0);\n"
            'font: 8pt "MS PGothic";\n'
            'font: 16pt "MS Shell Dlg 2";'
        )
        self.yellowSliderText.setWordWrap(True)
        self.yellowSliderText.setObjectName("label_5")

        # spawning text that says "Red Bell"
        self.redSliderText = QtWidgets.QLabel(Dialog)
        self.redSliderText.setGeometry(QtCore.QRect(660, 280, 51, 61))
        self.redSliderText.setAutoFillBackground(False)
        self.redSliderText.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "background-color: rgba(255, 255, 255, 0);\n"
            'font: 8pt "MS PGothic";\n'
            'font: 16pt "MS Shell Dlg 2";'
        )
        self.redSliderText.setWordWrap(True)
        self.redSliderText.setObjectName("label_6")

        # setting the layer order of elements in window
        self.logo.raise_()
        self.resetButton.raise_()
        self.lcdTimer.raise_()
        self.progressBar.raise_()
        self.roundIndicatorColor.raise_()
        self.playButton.raise_()
        self.graph.raise_()
        self.redSlider.raise_()
        self.yellowSlider.raise_()
        self.greenSlider.raise_()
        self.greenSliderText.raise_()
        self.yellowSliderText.raise_()
        self.redSliderText.raise_()
        self.directionsText.raise_()

        self.retranslateUi(Dialog)
        self.playButton.clicked.connect(self.lcdTimer.update)
        self.resetButton.clicked.connect(self.lcdTimer.update)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.playButton, self.resetButton)
        Dialog.setTabOrder(self.resetButton, self.roundIndicatorColor)

    def retranslateUi(self, Dialog):
        # setting the text of each element (if there is any)
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "9Round Bell System"))
        self.directionsText.setText(
            _translate(
                "Dialog",
                "DIRECTIONS: Turn on the physical bell in the studio."
                "Quickly run to the computer and press the PLAY button "
                "when you hear the first sound out of the physical bell. "
                "This program will run in tandem with the physical bell "
                "and should have no issues. If you need to stop the physical "
                "bell for any reason, click the RESET button. This will stop "
                "the program from running and reset the volume to 100. ",
            )
        )
        self.playButton.setText(_translate("Dialog", "PLAY"))
        self.resetButton.setText(_translate("Dialog", "RESET"))
        self.greenSliderText.setText(_translate("Dialog", "Green Bell/Start of Round"))
        self.yellowSliderText.setText(_translate("Dialog", "Yellow bell"))
        self.redSliderText.setText(_translate("Dialog", "Red bell"))

    # all this above is initializing the formatting to look pretty <3
    def UpdateButtonStyle(self):
        print(main.query())
        self.playButton.setStyleSheet("background-color: %s" % main.query()[2][2])

    def runVolumeController(self):
        main.restartTime()
        main.run()

    x = 0

    def playButtonLogic(self):
        if self.x == 0:
            self.volumeThread = twt.thread_with_trace(target=self.runVolumeController)
            self.volumeThread.start()
            self.playButton.setText(
                QtCore.QCoreApplication.translate("Dialog", "PLAYING")
            )
            self.x = 1
        else:
            print("you already have an instance running!")

    def resetButtonLogic(self):
        self.volumeThread.kill()
        volumeController.setVolume(75)
        self.playButton.setText(QtCore.QCoreApplication.translate("Dialog", "PLAY"))
        self.x = 0


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.__init__()
    Dialog.show()
    sys.exit(app.exec_())
