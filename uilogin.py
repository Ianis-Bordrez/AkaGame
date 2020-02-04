from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QMessageBox
import sys
from database import Database
import uicreateaccount

class WindowLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitLogin()

    def InitLogin(self):
        self.setGeometry(600,200,500,300)

        self.lineedit1 = QLineEdit(self)
        self.lineedit1.setPlaceholderText("Please Enter Your name")
        self.lineedit1.setGeometry(140, 50, 200, 30)

        self.lineedit2 = QLineEdit(self)
        self.lineedit2.setPlaceholderText("Please Enter Your password")
        self.lineedit2.setGeometry(140, 100, 200, 30)

        self.button=QPushButton("Login",self)
        self.button.move(180,150)
        self.button.clicked.connect(self.btn_login)

        self.button=QPushButton("Create Account",self)
        self.button.move(180,200)
        self.button.clicked.connect(self.btn_create_account)
        
        self.show()

    def btn_login(self):
        pass

    def btn_create_account(self):
        self.close()
        self.next= uicreateaccount.WindowCreateAccount()
