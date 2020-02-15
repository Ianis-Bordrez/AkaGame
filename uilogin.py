from PyQt5.QtWidgets import QApplication, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
import ui
from database import Database

import constinfo
import uicreateaccount
import uimainmenu
import uicreateplayer


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
        self.username.setGeometry(510, 200, 260, 30)
        self.username.setStyleSheet(
            "background-color : transparent; color : black; border : 1px solid black; border-radius: 5px; font-size : 17px")
        self.username.setAlignment(Qt.AlignCenter)
        self.username.setMaxLength(24)

        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Please Enter Your password")
        self.password.setGeometry(510, 250, 260, 30)
        self.password.setStyleSheet(
            "background-color : transparent; color : black; border : 1px solid black; border-radius: 5px; font-size : 17px")
        self.password.setAlignment(Qt.AlignCenter)
        self.password.setMaxLength(24)
        self.password.setEchoMode(QLineEdit.Password)

    def init_button(self):
        self.btn_login = QPushButton("Login", self)
        self.btn_login.resize(150, 60)
        self.btn_login.move(565, 300)
        self.btn_login.setStyleSheet("QPushButton { background-color: transparent; font-size: 20px; border : 2px solid black; border-radius : 20px }"
                                     "QPushButton:hover { background-color: rgba(50, 50, 50, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }"
                                     "QPushButton:pressed { background-color: rgba(250, 250, 250, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }")
        self.btn_login.clicked.connect(self.login)

        self.btn_create_account = QPushButton("Create Account", self)
        self.btn_create_account.resize(150, 60)
        self.btn_create_account.move(565, 370)
        self.btn_create_account.setStyleSheet("QPushButton { background-color: transparent; font-size: 20px; border : 2px solid black; border-radius : 20px }"
                                              "QPushButton:hover { background-color: rgba(50, 50, 50, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }"
                                              "QPushButton:pressed { background-color: rgba(250, 250, 250, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }")
        self.btn_create_account.clicked.connect(self.create_account)

        self.buttonview = QPushButton(self)
        self.buttonview.resize(33, 19)
        self.buttonview.move(775, 257)
        self.buttonview.setStyleSheet(
            "background-image: url(img/view.png);  background-color: transparent")
        self.buttonview.clicked.connect(self.passShow)

    def passShow(self):
        self.buttonview.setCheckable(True)
        if self.buttonview.isChecked():
            self.password.setEchoMode(QLineEdit.Normal)
        else:
            self.password.setEchoMode(QLineEdit.Password)

    def login(self):
        if self.check_login(self.username.text(), self.password.text()):
            self.close()
            if constinfo.player_id:
                self.next = uimainmenu.WindowMainMenu()
            else:
                self.next = uicreateplayer.WindowCreatePlayer()

    def create_account(self):
        self.close()
        self.next = uicreateaccount.WindowCreateAccount()

    def check_login(self, username, password):
        myDataBase = Database(constinfo.mysql_config)
        myDataBase.connect()

        query = f"SELECT id FROM account WHERE login='{username}' AND password='{password}'"
        account_id = myDataBase.get(query)
        if account_id is None:
            QMessageBox.about(self, "Connection", "Wrong username or password")
            return False
        constinfo.account_id = account_id[0]

        # QMessageBox.about(self, "Connection", "Successful connection")
        query = f"SELECT id FROM player WHERE account_id={account_id[0]}"
        player = myDataBase.get(query)
        constinfo.player_id = player[0]
        return True
