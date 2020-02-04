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

        self.lineedit1 = QLineEdit(self)
        self.lineedit1.setPlaceholderText("Please Enter Your name")
        self.lineedit1.setGeometry(540, 200, 200, 30)

        self.lineedit2 = QLineEdit(self)
        self.lineedit2.setPlaceholderText("Please Enter Your password")
        self.lineedit2.setGeometry(540, 250, 200, 30)

        self.button = QPushButton("Login", self)
        self.button.resize(100, 60)
        self.button.move(590, 300)
        self.button.clicked.connect(self.btn_login)

        self.button = QPushButton("Create Account", self)
        self.button.resize(100, 60)
        self.button.move(590, 370)
        self.button.clicked.connect(self.btn_create_account)

        self.show()

    def btn_login(self):
        username = self.username.text()
        password = self.password.text()
        if len(username) < 4 or len(password) < 4:
            return False

        myDataBase = Database(constinfo.mysql_config)
        myDataBase.connect()

        query = f"SELECT login,password FROM account WHERE login='{username}'"
        result = myDataBase.get(query)
        print(result)
        if result is None:
            QMessageBox.about(self, "Connection",
                              "Wrong username or password")
        else:
            if self.check_login(self, username, password):
                pass

    def btn_create_account(self):
        self.close()
        self.next = uicreateaccount.WindowCreateAccount()

    def check_login(self, username, password):

        QMessageBox.about(self, "Create Account", "Email not valid")
        return False
