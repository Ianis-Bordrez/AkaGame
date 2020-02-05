from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QMessageBox, QLabel
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QMessageBox
import sys
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import *
import ui
from PyQt5.QtWidgets import QLineEdit, QPushButton, QMessageBox
from database import Database

import constinfo
import uicreateaccount


class WindowLogin(ui.Window):
    def __init__(self):
        ui.Window.__init__(self, "Akagame | Connection")
        self.init_window()
        self.init_background("img/imgbckg.jpg")
        self.init_lineedit()
        self.init_button()
        self.show()

    def init_lineedit(self):
        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Please Enter Your name")
        self.username.setGeometry(540, 200, 200, 30)
        self.username.setStyleSheet(
            "background-color : transparent; color : black; border : 1px solid black; border-radius: 5px;")

        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Please Enter Your password")
        self.password.setGeometry(540, 250, 200, 30)
        self.password.setStyleSheet(
            "background-color : transparent; color : black; border : 1px solid black; border-radius: 5px;")

    def init_button(self):
        self.btn_login = QPushButton("Login", self)
        self.btn_login.resize(150, 60)
        self.btn_login.move(565, 300)
        self.btn_login.setStyleSheet(
            "background-color: transparent; font-size: 20px; border : 2px solid black; border-radius : 20px")
        self.btn_login.clicked.connect(self.login)

        self.btn_create_account = QPushButton("Create Account", self)
        self.btn_create_account.resize(150, 60)
        self.btn_create_account.move(565, 370)
        self.btn_create_account.setStyleSheet(
            "background-color: transparent; font-size: 20px; border : 2px solid black; border-radius : 20px")
        self.btn_create_account.clicked.connect(self.create_account)

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
