import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import main

# Run this with python.exe


class App(QMainWindow):
    @pyqtSlot()
    def on_click(self):
        main.run()

    def __init__(self):
        super().__init__()
        self.title = "PyQt5 status bar example - pythonspot.com"
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage("Message in statusbar.")
        button = QPushButton("PyQt5 button", self)
        button.setToolTip("This is an example button")
        button.move(100, 70)
        button.clicked.connect(self.on_click)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
