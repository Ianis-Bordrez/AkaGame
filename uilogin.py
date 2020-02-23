from PyQt5.QtWidgets import QLineEdit, QPushButton, QMessageBox, QLabel, QWidget
from PyQt5.QtCore import Qt
from database import Database
import ui
import constinfo
import uicreateaccount
import uimainmenu
import uicreateplayer
import uimainmenuteatcher


class WindowLogin(ui.Window):
    def __init__(self):
        ui.Window.__init__(self, "Akagame | Connection")
        self.init_window()
        self.init_background("img/imgbckg.jpg")

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.init_lineedit()
        self.init_button()
        self.init_label()
        self.show()

    def init_label(self):
        stylesheet = "font-size : 17px;"
        self.lbl_username = QLabel(self.centralwidget)
        self.lbl_username.setGeometry(350, 205, 150, 30)
        self.lbl_username.setText("Nom d'utilisateur")
        self.lbl_username.setAlignment(Qt.AlignRight)
        self.lbl_username.setStyleSheet(constinfo.stylesheet_main_button)

        self.lbl_password = QLabel(self.centralwidget)
        self.lbl_password.setGeometry(350, 255, 150, 30)
        self.lbl_password.setText("Mot de passe")
        self.lbl_password.setAlignment(Qt.AlignRight)
        self.lbl_password.setStyleSheet(constinfo.stylesheet_main_button)

    def init_lineedit(self):
        self.username = QLineEdit(self.centralwidget)
        self.username.setPlaceholderText("Please Enter Your name")
        self.username.setGeometry(510, 200, 260, 30)
        self.username.setStyleSheet(constinfo.stylesheet_lineedit)
        self.username.setAlignment(Qt.AlignCenter)
        self.username.setMaxLength(24)

        self.password = QLineEdit(self.centralwidget)
        self.password.setPlaceholderText("Please Enter Your password")
        self.password.setGeometry(510, 250, 260, 30)
        self.password.setStyleSheet(constinfo.stylesheet_lineedit)
        self.password.setAlignment(Qt.AlignCenter)
        self.password.setMaxLength(24)
        self.password.setEchoMode(QLineEdit.Password)

    def init_button(self):
        self.btn_login = QPushButton("Login", self.centralwidget)
        self.btn_login.resize(150, 60)
        self.btn_login.move(565, 300)
        self.btn_login.setStyleSheet(constinfo.stylesheet_main_button)
        self.btn_login.clicked.connect(self.login)

        self.btn_create_account = QPushButton("Create Account", self.centralwidget)
        self.btn_create_account.resize(150, 60)
        self.btn_create_account.move(565, 370)
        self.btn_create_account.setStyleSheet(constinfo.stylesheet_main_button)
        self.btn_create_account.clicked.connect(self.create_account)

        self.buttonview = QPushButton(self.centralwidget)
        self.buttonview.resize(33, 19)
        self.buttonview.move(775, 257)
        self.buttonview.setStyleSheet("background-image: url(img/view.png);  background-color: transparent;")
        self.buttonview.clicked.connect(self.passShow)
        self.buttonview.setCheckable(True)

    def passShow(self):
        if self.buttonview.isChecked():
            self.password.setEchoMode(QLineEdit.Normal)
        else:
            self.password.setEchoMode(QLineEdit.Password)

    def login(self):
        if self.check_login(self.username.text(), self.password.text()):
            self.close()
            if constinfo.account_status == "TEATCHER":
                self.next = uimainmenuteatcher.WindowTeatcher()

            elif constinfo.player_id:
                self.next = uimainmenu.WindowMainMenu()
            else:
                self.next = uicreateplayer.WindowCreatePlayer()

    def create_account(self):
        self.close()
        self.next = uicreateaccount.WindowCreateAccount()

    def check_login(self, username, password):

        query = f"SELECT id, status, subject FROM account WHERE login='{username}' AND password='{password}'"
        account_info = self.myDataBase.get(query)
        if account_info is None:
            QMessageBox.about(self, "Connection", "Wrong username or password")
            return False

        constinfo.account_id = account_info[0][0]
        constinfo.account_status = account_info[0][1].pop()
        constinfo.teatcher_subject = account_info[0][2].pop()

        query = f"SELECT id FROM player WHERE account_id={constinfo.account_id}"
        player = self.myDataBase.get(query)
        if player != None:
            constinfo.player_id = player[0]
        return True
