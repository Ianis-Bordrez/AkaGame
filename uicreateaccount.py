from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QMessageBox, QLabel, QComboBox, QWidget
from PyQt5.QtCore import Qt, QTimer
from database import Database
import uilogin
import constinfo
import ui


class WindowCreateAccount(ui.Window):
    def __init__(self):
        ui.Window.__init__(self, "Akagame | Create account")
        self.init_window()
        self.init_background("img/imgbckg.jpg")
        self.init_title("Création de compte")

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.init_lineedit()
        self.init_error_field()
        self.init_label()
        self.init_button()

        self.question_manager_lbl_success = QLabel(self.centralwidget)
        self.question_manager_lbl_success.setGeometry(500, 500, 200, 30)

        self.btn_return = ui.ReturnButton(uilogin.WindowLogin, self.close, parent=self.centralwidget)

        self.show()

    def init_label(self):
        self.lbl_username = QLabel(self.centralwidget)
        self.lbl_username.setGeometry(330, 205, 150, 30)
        self.lbl_username.setText("Nom d'utilisateur")
        self.lbl_username.setAlignment(Qt.AlignRight)
        self.lbl_username.setStyleSheet("font-size : 17px;")

        self.lbl_password = QLabel(self.centralwidget)
        self.lbl_password.setGeometry(330, 275, 150, 30)
        self.lbl_password.setText("Mot de passe")
        self.lbl_password.setAlignment(Qt.AlignRight)
        self.lbl_password.setStyleSheet("font-size : 17px;")

        self.lbl_email = QLabel(self.centralwidget)
        self.lbl_email.setGeometry(330, 345, 150, 30)
        self.lbl_email.setText("Email")
        self.lbl_email.setAlignment(Qt.AlignRight)
        self.lbl_email.setStyleSheet("font-size : 17px;")

    def init_lineedit(self):
        self.username = QLineEdit(self.centralwidget)
        self.username.setPlaceholderText("Please Enter Your username")
        self.username.setGeometry(490, 200, 300, 30)
        self.username.setStyleSheet(constinfo.stylesheet_lineedit)
        self.username.setAlignment(Qt.AlignCenter)

        self.password = QLineEdit(self.centralwidget)
        self.password.setPlaceholderText("Please Enter Your password")
        self.password.setGeometry(490, 270, 300, 30)
        self.password.setStyleSheet(constinfo.stylesheet_lineedit)
        self.password.setAlignment(Qt.AlignCenter)
        self.password.setEchoMode(QLineEdit.Password)

        self.email = QLineEdit(self.centralwidget)
        self.email.setPlaceholderText("Please Enter Your Emai")
        self.email.setGeometry(490, 340, 300, 30)
        self.email.setStyleSheet(constinfo.stylesheet_lineedit)
        self.email.setAlignment(Qt.AlignCenter)

        self.teatcher = QLineEdit(self.centralwidget)
        self.teatcher.setPlaceholderText("Please Enter Your Teatcher's Code")
        self.teatcher.setGeometry(490, 775, 300, 30)
        self.teatcher.setStyleSheet(
            "background-color : transparent; border : 2px solid white; border-radius: 5px; font-size : 19px; color : white;"
        )
        self.teatcher.setAlignment(Qt.AlignCenter)

    def init_error_field(self):
        self.username_error_field = QLabel(self.centralwidget)
        self.username_error_field.setText("")
        self.username_error_field.setGeometry(440, 230, 400, 30)
        self.username_error_field.setStyleSheet("color: red; text-align : center")
        self.username_error_field.setAlignment(Qt.AlignCenter)

        self.password_error_field = QLabel(self.centralwidget)
        self.password_error_field.setText("")
        self.password_error_field.setGeometry(440, 300, 400, 30)
        self.password_error_field.setStyleSheet("color : red; text-align : center")
        self.password_error_field.setAlignment(Qt.AlignCenter)

        self.email_error_field = QLabel(self.centralwidget)
        self.email_error_field.setText("")
        self.email_error_field.setGeometry(440, 370, 400, 30)
        self.email_error_field.setStyleSheet("color : red; text-align : center")
        self.email_error_field.setAlignment(Qt.AlignCenter)

        self.teatcher_error_field = QLabel(self.centralwidget)
        self.teatcher_error_field.setText("")
        self.teatcher_error_field.setGeometry(440, 230, 400, 30)
        self.teatcher_error_field.setStyleSheet("color: red; text-align : center")
        self.teatcher_error_field.setAlignment(Qt.AlignCenter)

    def init_button(self):
        self.btn_create = QPushButton("Create", self.centralwidget)
        self.btn_create.resize(150, 60)
        self.btn_create.move(565, 400)
        self.btn_create.clicked.connect(self.create_account)
        self.btn_create.setStyleSheet(constinfo.stylesheet_main_button)

        self.buttonview = QPushButton(self)
        self.buttonview.resize(33, 19)
        self.buttonview.move(800, 275)
        self.buttonview.setStyleSheet("background-image: url(img/view.png);  background-color: transparent")
        self.buttonview.clicked.connect(self.passShow)
        self.buttonview.setCheckable(True)

    def qwidgetwindow(self):
        self.button_create_teatcher = QPushButton("Create a teacher account", self.centralwidget)
        self.button_create_teatcher.resize(300, 70)
        self.button_create_teatcher.move(490, 700)
        self.button_create_teatcher.setStyleSheet(constinfo.stylesheet_main_button)
        self.button_create_teatcher.show()

        self.scroll_subject_choose = QComboBox(self.centralwidget)
        self.scroll_subject_choose.addItem("FRENCH")
        self.scroll_subject_choose.addItem("MATHS")
        self.scroll_subject_choose.addItem("HISTORY")
        self.scroll_subject_choose.setGeometry(590, 535, 100, 30)
        self.scroll_subject_choose.setStyleSheet(
            "QComboBox {  border-radius: 3px; }" "QComboBox QAbstractItemView {  border-radius: 3px; }"
        )
        self.scroll_subject_choose.show()

    def passShow(self):
        if self.buttonview.isChecked():
            self.password.setEchoMode(QLineEdit.Normal)
        else:
            self.password.setEchoMode(QLineEdit.Password)

    def error_username(self):
        self.username_error_field.setText("Your username must be between 5 and 24 characters.")

    def error_password(self):
        self.password_error_field.setText("Your password must be between 5 and 24 characters.")

    def error_email(self):
        self.email_error_field.setText("Email not valid.")

    def error_teatcher(self):
        self.teatcher_error_field.setText("Incorrect code.")

    def valid_username(self):
        self.username_error_field.setText("")

    def valid_password(self):
        self.password_error_field.setText("")

    def valid_email(self):
        self.email_error_field.setText("")

    def valid_teatcher(self):
        self.teatcher_error_field.setText("")

    def query_create_account(self, table, query, username, password, email, status, subject):
        if subject != "NONE":
            subject = self.scroll_subject_choose.currentText()
        self.myDataBase.post(query, (username, password, email, status, subject))
        QMessageBox.about(self, "Connection", "Account created Successfully")
        self.close()
        self.next = uilogin.WindowLogin()

    def create_account(self):
        username = self.username.text()
        password = self.password.text()
        email = self.email.text()
        code = self.teatcher.text()

        if self.check_account(username, password, email, code):

            table = "account"
            query = constinfo.SQL_INSERT.format(
                columns=",".join(constinfo.columns_create_account),
                table=table,
                placeholders=",".join(["%s" for i in range(len(constinfo.columns_create_account))]),
            )
            if code == "ok":
                self.qwidgetwindow()
                status = "TEATCHER"
                subject = self.scroll_subject_choose.currentText()
                self.button_create_teatcher.clicked.connect(
                    lambda: self.query_create_account(table, query, username, password, email, status, subject)
                )
            else:
                status = "STUDENT"
                subject = "NONE"
                self.query_create_account(table, query, username, password, email, status, subject)

    def timer_account_error(self, sentence):
        self.validate_timer = QTimer()
        self.validate_timer.setInterval(4000)
        self.validate_timer.timeout.connect(self.timer_account_error_stop)
        self.validate_timer.start()

        self.question_manager_lbl_success.setText(sentence)
        self.question_manager_lbl_success.show()

    def timer_account_error_stop(self):
        self.validate_timer.stop()
        self.question_manager_lbl_success.hide()

    def check_account(self, username, password, email, code):
        if (
            self.check_username(username)
            and self.check_password(password)
            and self.check_email(email)
            and self.check_teatcher_code(code)
        ):
            if not self.myDataBase.get(f"SELECT login FROM account WHERE login='{username}'"):
                return True
            else:
                self.timer_account_error("Le nom d'utilisateur est déjà utilisé.")
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

        result = re.search(r"\w+@\w+", email)
        if result:
            self.valid_email()
            return True

        self.error_email()
        return False

    def check_teatcher_code(self, code):
        if code == "ok" or code == "":
            return True
        return False

