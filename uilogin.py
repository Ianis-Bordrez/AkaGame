from PyQt5.QtWidgets import QLineEdit, QPushButton, QMessageBox
from database import Database

import constinfo
import uicreateaccount
import ui


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

        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Please Enter Your password")
        self.password.setGeometry(540, 250, 200, 30)

    def init_button(self):
        self.btn_login = QPushButton("Login", self)
        self.btn_login.resize(100, 60)
        self.btn_login.move(590, 300)
        self.btn_login.clicked.connect(self.login)

        self.btn_create_account = QPushButton("Create Account", self)
        self.btn_create_account.resize(100, 60)
        self.btn_create_account.move(590, 370)
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
