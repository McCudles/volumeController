import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 400)
        Dialog.setMinimumSize(QtCore.QSize(800, 400))
        Dialog.setMaximumSize(QtCore.QSize(800, 400))
        font = QtGui.QFont()
        font.setPointSize(8)
        Dialog.setFont(font)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-color: rgb(54, 52, 53);\n"
"selection-color: rgb(28, 39, 255);")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 360, 781, 31))
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet("color: rgb(255, 255, 255);")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.playButton = QtWidgets.QPushButton(Dialog)
        self.playButton.setGeometry(QtCore.QRect(10, 120, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.playButton.setFont(font)
        self.playButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.playButton.setStyleSheet("background-color: rgb(6, 176, 37);\n"
"\n"
"font: 36pt \"Dubai\";")
        self.playButton.setObjectName("playButton")
        self.pauseButton = QtWidgets.QPushButton(Dialog)
        self.pauseButton.setGeometry(QtCore.QRect(10, 190, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pauseButton.setFont(font)
        self.pauseButton.setAutoFillBackground(False)
        self.pauseButton.setStyleSheet("\n"
"font: 36pt \"Dubai\";\n"
"color: rgb(230, 230, 230);\n"
"background-color: rgb(117, 117, 117);")
        self.pauseButton.setObjectName("pauseButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, -10, 271, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./biglogowhite.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 290, 171, 61))
        self.lcdNumber.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.roundIndicatorColor = QtWidgets.QGraphicsView(Dialog)
        self.roundIndicatorColor.setGeometry(QtCore.QRect(640, 110, 141, 141))
        self.roundIndicatorColor.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.roundIndicatorColor.setObjectName("roundIndicatorColor")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(440, 150, 181, 61))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 8pt \"MS PGothic\";\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.playButton.raise_()
        self.pauseButton.raise_()
        self.label.raise_()
        self.lcdNumber.raise_()
        self.progressBar.raise_()
        self.roundIndicatorColor.raise_()
        self.label_2.raise_()

        self.retranslateUi(Dialog)
        self.playButton.clicked.connect(self.lcdNumber.update) # type: ignore
        self.pauseButton.clicked.connect(self.lcdNumber.update) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.playButton, self.pauseButton)
        Dialog.setTabOrder(self.pauseButton, self.roundIndicatorColor)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.playButton.setText(_translate("Dialog", "PLAY"))
        self.pauseButton.setText(_translate("Dialog", "PAUSE"))
        self.label_2.setText(_translate("Dialog", "round color >>>"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
