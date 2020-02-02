from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from PyQt5 import QtGui
import sys


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Window"
        self.top = 50
        self.left = 100
        self.width = 1000
        self.height = 1000
        self.initWindow()

    def initWindow(self):
        # self.windowIcon(QtGuy.QIcon("lienDeL'icone"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.CreateLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

        self.show()

    def CreateLayout(self):
        self.groupBox = QGroupBox("What is your favorite sport ?")
        hboxlayout = QHBoxLayout()

        button = QPushButton("Boxe", self)
        button.setIcon(QtGui.QIcon("boxe.png"))
        button.setIconSize(QtCore.QSize(40, 40))
        button.setMinimumHeight(40)
        hboxlayout.addWidget(button)

        button1 = QPushButton("Snowboard", self)
        button1.setIcon(QtGui.QIcon("snow.jpg"))
        button1.setIconSize(QtCore.QSize(40, 40))
        button1.setMinimumHeight(40)
        hboxlayout.addWidget(button1)

        button2 = QPushButton("Badminton", self)
        button2.setIcon(QtGui.QIcon("bad.jpg"))
        button2.setIconSize(QtCore.QSize(40, 40))
        button2.setMinimumHeight(40)
        hboxlayout.addWidget(button2)

        self.groupBox.setLayout(hboxlayout)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
