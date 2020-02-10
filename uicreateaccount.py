from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QMessageBox, QLabel
from PyQt5.QtCore import Qt
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
        self.init_error_field()
        self.init_button()
        self.show()

    def init_lineedit(self):
        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Please Enter Your username")
        self.username.setGeometry(490, 100, 300, 30)
        self.username.setStyleSheet(
            "background-color : transparent; color : black; border : 1px solid black; border-radius: 5px; font-size : 17px")

        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Please Enter Your password")
        self.password.setGeometry(490, 170, 300, 30)
        self.password.setStyleSheet(
            "background-color : transparent; color : black; border : 1px solid black; border-radius: 5px; font-size : 17px")

        self.email = QLineEdit(self)
        self.email.setPlaceholderText("Please Enter Your Emai")
        self.email.setGeometry(490, 240, 300, 30)
        self.email.setStyleSheet(
            "background-color : transparent; color : black; border : 1px solid black; border-radius: 5px; font-size : 17px")

    def init_error_field(self):
        self.username_error_field = QLabel(self)
        self.username_error_field.setText("")
        self.username_error_field.setGeometry(440, 130, 400, 30)
        self.username_error_field.setStyleSheet(
            "color: red; text-align : center")
        self.username_error_field.setAlignment(Qt.AlignCenter)

        self.password_error_field = QLabel(self)
        self.password_error_field.setText("")
        self.password_error_field.setGeometry(440, 200, 400, 30)
        self.password_error_field.setStyleSheet(
            "color : red; text-align : center")
        self.password_error_field.setAlignment(Qt.AlignCenter)

        self.email_error_field = QLabel(self)
        self.email_error_field.setText("")
        self.email_error_field.setGeometry(440, 270, 400, 30)
        self.email_error_field.setStyleSheet(
            "color : red; text-align : center")
        self.email_error_field.setAlignment(Qt.AlignCenter)

    def init_button(self):
        self.btn_create = QPushButton("Create", self)
        self.btn_create.setGeometry(200, 300, 100, 30)
        self.btn_create.clicked.connect(self.create_account)

        self.btn_return = QPushButton("Return", self)
        self.btn_return.move(100, 400)
        self.btn_return.clicked.connect(self.return_login)

    def error_username(self):
        self.username_error_field.setText(
            "Your username must be between 5 and 24 characters.")

    def error_password(self):
        self.password_error_field.setText(
            "Your password must be between 5 and 24 characters.")

    def error_email(self):
        self.email_error_field.setText(
            "Email not valid.")

    def valid_username(self):
        self.username_error_field.setText(
            "")

    def valid_password(self):
        self.password_error_field.setText(
            "")

    def valid_email(self):
        self.email_error_field.setText(
            "")

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
        if self.check_username(username) and self.check_password(password) and self.check_email(email):
            return True
        return False

    def check_username(self, username):
        if len(username) > 24 or len(username) < 5:
            self.error_username()

            return False
        self.valid_username()
        return True

    def check_password(self, password):
        if len(password) > 24 or len(password) < 5:
            self.error_password()
            return False
        self.valid_password()
        return True

    def check_email(self, email):
        import re
        result = re.search(r'\w+@\w+', email)
        if result:
            self.valid_email()
            return True

        self.error_email()
        return False

    def return_login(self):
        self.close()
        self.next = uilogin.WindowLogin()
