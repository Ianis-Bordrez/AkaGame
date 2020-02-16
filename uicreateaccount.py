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
        self.username.setGeometry(490, 200, 300, 30)
        self.username.setStyleSheet(
            "background-color : transparent; color : black; border : 1px solid black; border-radius: 5px; font-size : 17px")
        self.username.setAlignment(Qt.AlignCenter)

        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Please Enter Your password")
        self.password.setGeometry(490, 270, 300, 30)
        self.password.setStyleSheet(
            "background-color : transparent; color : black; border : 1px solid black; border-radius: 5px; font-size : 17px")
        self.password.setAlignment(Qt.AlignCenter)
        self.password.setEchoMode(QLineEdit.Password)

        self.email = QLineEdit(self)
        self.email.setPlaceholderText("Please Enter Your Emai")
        self.email.setGeometry(490, 340, 300, 30)
        self.email.setStyleSheet(
            "background-color : transparent; color : black; border : 1px solid black; border-radius: 5px; font-size : 17px")
        self.email.setAlignment(Qt.AlignCenter)

        self.teatcher = QLineEdit(self)
        self.teatcher.setPlaceholderText("Please Enter Your Teatcher's Code")
        self.teatcher.setGeometry(490, 680, 300, 30)
        self.teatcher.setStyleSheet(
            "background-color : transparent; border : 2px solid white; border-radius: 5px; font-size : 19px; color : white;")
        self.teatcher.setAlignment(Qt.AlignCenter)

    def init_error_field(self):
        self.username_error_field = QLabel(self)
        self.username_error_field.setText("")
        self.username_error_field.setGeometry(440, 230, 400, 30)
        self.username_error_field.setStyleSheet(
            "color: red; text-align : center")
        self.username_error_field.setAlignment(Qt.AlignCenter)

        self.password_error_field = QLabel(self)
        self.password_error_field.setText("")
        self.password_error_field.setGeometry(440, 300, 400, 30)
        self.password_error_field.setStyleSheet(
            "color : red; text-align : center")
        self.password_error_field.setAlignment(Qt.AlignCenter)

        self.email_error_field = QLabel(self)
        self.email_error_field.setText("")
        self.email_error_field.setGeometry(440, 370, 400, 30)
        self.email_error_field.setStyleSheet(
            "color : red; text-align : center")
        self.email_error_field.setAlignment(Qt.AlignCenter)

        self.teatcher_error_field = QLabel(self)
        self.teatcher_error_field.setText("")
        self.teatcher_error_field.setGeometry(440, 230, 400, 30)
        self.teatcher_error_field.setStyleSheet(
            "color: red; text-align : center")
        self.teatcher_error_field.setAlignment(Qt.AlignCenter)

    def init_button(self):
        self.btn_create = QPushButton("Create", self)
        self.btn_create.resize(150, 60)
        self.btn_create.move(565, 400)
        self.btn_create.clicked.connect(self.create_account)
        self.btn_create.setStyleSheet("QPushButton { background-color: transparent; font-size: 20px; border : 2px solid black; border-radius : 20px }"
                                      "QPushButton:hover { background-color: rgba(50, 50, 50, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }"
                                      "QPushButton:pressed { background-color: rgba(250, 250, 250, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }")

        self.btn_return = QPushButton("Return", self)
        self.btn_return.resize(150, 60)
        self.btn_return.move(565, 470)
        self.btn_return.clicked.connect(self.return_login)
        self.btn_return.setStyleSheet("QPushButton { background-color: transparent; font-size: 20px; border : 2px solid black; border-radius : 20px }"
                                      "QPushButton:hover { background-color: rgba(50, 50, 50, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }"
                                      "QPushButton:pressed { background-color: rgba(250, 250, 250, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }")

        self.buttonview = QPushButton(self)
        self.buttonview.resize(33, 19)
        self.buttonview.move(800, 275)
        self.buttonview.setStyleSheet(
            "background-image: url(img/view.png);  background-color: transparent")
        self.buttonview.clicked.connect(self.passShow)

    def passShow(self):
        self.buttonview.setCheckable(True)
        if self.buttonview.isChecked():
            self.password.setEchoMode(QLineEdit.Normal)
        else:
            self.password.setEchoMode(QLineEdit.Password)

    def error_username(self):
        self.username_error_field.setText(
            "Your username must be between 5 and 24 characters.")

    def error_password(self):
        self.password_error_field.setText(
            "Your password must be between 5 and 24 characters.")

    def error_email(self):
        self.email_error_field.setText(
            "Email not valid.")

    def error_teatcher(self):
        self.teatcher_error_field.setText(
            "Incorrect code.")

    def valid_username(self):
        self.username_error_field.setText(
            "")

    def valid_password(self):
        self.password_error_field.setText(
            "")

    def valid_email(self):
        self.email_error_field.setText(
            "")

    def valid_teatcher(self):
        self.teatcher_error_field.setText(
            "")

    def create_account(self):
        username = self.username.text()
        password = self.password.text()
        email = self.email.text()
        code = self.teatcher.text()

        if self.check_account(username, password, email, code):

            myDataBase = Database(constinfo.mysql_config)
            myDataBase.connect()
            table = 'account'
            query = constinfo.SQL_INSERT.format(
                columns=','.join(constinfo.columns_create_account), table=table,
                placeholders=','.join(['%s' for i in range(
                    len(constinfo.columns_create_account))])
            )

            status = "STUDENT"
            if code == "ok":
                status = "TEATCHER"

            myDataBase.post(query, (username, password, email, status))

            QMessageBox.about(self, "Connection",
                              "Account created Successfully")

            self.close()
            self.next = uilogin.WindowLogin()

    def check_account(self, username, password, email, code):
        if self.check_username(username) and self.check_password(password) and self.check_email(email) and self.check_teatcher_code(code):
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

    def check_teatcher_code(self, code):
        if code == "ok" or code == "":
            return True
        print("marchepas")
        return False

    def return_login(self):
        self.close()
        self.next = uilogin.WindowLogin()
