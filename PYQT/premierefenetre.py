from PyQt5.QtWidgets import QMainWindow, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from PyQt5 import QtGui


class Window(QMainWindow):
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
        self.BouttonPrSourisDessus()
        self.BouttonPrPrint()
        self.BouttonPrFermer()
        self.CreateLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

        self.show()

    def BouttonPrSourisDessus(self):
        button = QPushButton("Boutton message", self)
        button.setGeometry(QRect(100, 100, 120, 50))
        # button.setIcon(QtGui.QIcon("lienDeL'icone"))
        # button.setIconSize(QtCore.QSize(40.40))
        button.setToolTip("<h1>Dis Wallah<h1>")

    def BouttonPrPrint(self):
        button = QPushButton("Boutton Fonction(Print)", self)
        button.setGeometry(QRect(50, 50, 200, 50))
        button.clicked.connect(self.Print)

    def BouttonPrFermer(self):
        button = QPushButton("Boutton Fonction(Fermer l'app)", self)
        button.setGeometry(QRect(200, 200, 200, 50))
        button.clicked.connect(self.Exit)

    def Print(self):
        print("Dis Wallah")

    def CreateLayout(self):
        self.groupBox = QGroupBox("What is your favorite sport ?")
        hboxlayout = QHBoxLayout()

        button = QPushButton("Boxe", self)
        button.setMinimumHeight(40)
        hboxlayout.addWidget(button)

        button1 = QPushButton("Snowboard", self)
        button1.setMinimumHeight(40)
        hboxlayout.addWidget(button1)

        button3 = QPushButton("Badminton", self)
        button3.setMinimumHeight(40)
        hboxlayout.addWidget(button3)

        self.groupBox.setLayout(hboxlayout)

    def Exit(self):
        sys.exit()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
