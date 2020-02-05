import constinfo
import uicreateaccount
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
from database import Database
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush
import sys
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QMessageBox, QLabel
from PyQt5 import QtGui


class WindowLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitLogin()

    def InitLogin(self):

        self.setGeometry(600, 200, 1280, 800)
        self.setWindowTitle("AkaGame")

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("img/imgbckg.jpg"))
        self.label.setGeometry(0, 0, 1280, 800)

        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Please Enter Your name")
        self.username.setGeometry(540, 200, 200, 30)

        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Please Enter Your password")
        self.password.setGeometry(540, 250, 200, 30)

        self.btn_login = QPushButton("Login", self)
        self.btn_login.resize(100, 60)
        self.btn_login.move(590, 300)
        self.btn_login.clicked.connect(self.login)

        self.btn_create_account = QPushButton("Create Account", self)
        self.btn_create_account.resize(100, 60)
        self.btn_create_account.move(590, 370)
        self.btn_create_account.clicked.connect(self.create_account)

        self.show()

    def login(self):
        if self.check_login(self.username.text(), self.password.text()):
            pass

    def create_account(self):
        self.close()
        self.next = uicreateaccount.WindowCreateAccount()

    def check_login(self, username, password):
        myDataBase = Database(constinfo.mysql_config)
        myDataBase.connect()

        query = f"SELECT login,password FROM account WHERE login='{username}'"
        result = myDataBase.get(query)
        if result is None:
            QMessageBox.about(self, "Connection", "Wrong username or password")
            return False

        QMessageBox.about(self, "Connection", "Successful connection")
        return True
