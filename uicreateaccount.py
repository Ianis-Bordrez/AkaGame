from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QMessageBox
from database import Database
import uilogin
import constinfo
import ui


class WindowCreateAccount(ui.Window):
    def __init__(self):
        ui.Window.__init__(self, "Akagame | Create account")
        self.init_window()
        self.init_background("img/imgbckg.jpg")
        self.init_lineedit()
        self.init_button()
        self.show()

    def init_lineedit(self):
        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Please Enter Your username")
        self.username.setGeometry(200, 100, 200, 30)

        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Please Enter Your password")
        self.password.setGeometry(200, 150, 200, 30)

        self.email = QLineEdit(self)
        self.email.setPlaceholderText("Please Enter Your Emai")
        self.email.setGeometry(200, 200, 200, 30)

    def init_button(self):
        self.btn_create = QPushButton("Create", self)
        self.btn_create.setGeometry(200, 250, 100, 30)
        self.btn_create.clicked.connect(self.create_account)

        self.btn_return = QPushButton("Return", self)
        self.btn_return.move(100, 400)
        self.btn_return.clicked.connect(self.return_login)

    def create_account(self):
        username = self.username.text()
        password = self.password.text()
        email = self.email.text()

        if self.check_account(username, password, email):

            myDataBase = Database(constinfo.mysql_config)
            myDataBase.connect()
            table = 'account'
            query = constinfo.SQL_INSERT.format(
                columns=','.join(constinfo.columns_create_account), table=table,
                placeholders=','.join(['%s' for i in range(
                    len(constinfo.columns_create_account))])
            )
            myDataBase.post(query, (username, password, email))

            QMessageBox.about(self, "Connection",
                              "Account created Successfully")

            self.close()
            self.next = uilogin.WindowLogin()

    def check_account(self, username, password, email):
        if self.check_username(username) or self.check_password(password) or self.check_email(email):
            return True
        return False

    def check_username(self, username):
        if len(username) > 24 or len(username) < 5:
            QMessageBox.about(self, "Create Account",
                              "Your username must be between 5 and 24 characters.")
            return False

        return True

    def check_password(self, password):
        if len(password) > 24 or len(password) < 5:
            QMessageBox.about(self, "Create Account",
                              "Your password must be between 5 and 24 characters.")
            return False

        return True

        QMessageBox.about(self, "Create Account", "Password not valid")
        return False

    def check_email(self, email):
        import re
        result = re.search(r'\w+@\w+', email)
        if result:
            return True

        QMessageBox.about(self, "Create Account", "Email not valid")
        return False

    def return_login(self):
        self.close()
        self.next = uilogin.WindowLogin()
