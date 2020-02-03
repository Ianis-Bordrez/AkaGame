from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QMessageBox
import sys
from database import Database
import uiinsertDB


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Connexion"
        self.top = 50
        self.left = 100
        self.width = 1000
        self.height = 800

        self.initWindow()

    def initWindow(self):
        self.button = QPushButton("DB Connection Status", self)
        self.button.setGeometry(100, 100, 200, 50)
        self.button.clicked.connect(self.connectDB)

        self.button2 = QPushButton("DB Insert", self)
        self.button2.setGeometry(200, 200, 200, 50)
        self.button2.clicked.connect(self.insertDB)

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()

    def connectDB(self):
        try:
            mysql_config = {"host": "localhost", "user": "root",
                            "passwd": "", "database": "akagame"}
            myDataBase = Database(mysql_config)
            myDataBase.connect()
            QMessageBox.about(self, "Connection",
                              "Successfully connected to DB")
        except:
            QMessageBox.about(self, "Connection", "Not connected successfully")
            sys.exit()

    def insertDB(self):
        WindowConn = uiinsertDB.WindowConnect()
