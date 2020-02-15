from PyQt5.QtWidgets import QLineEdit, QPushButton, QLabel, QWidget, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QRect
from database import Database
import uimainmenu
import constinfo
import ui


class WindowCreatePlayer(ui.Window):
    def __init__(self):
        ui.Window.__init__(self, "AkaGame | Create Player")
        self.init_window()
        self.init_background("img/bckg_create_char.jpg")

        self.centralwidget = QWidget(self)
        self.sex = 0
        self.curr_char = 0
        self.char_img_m = ("char_m_1.png", "char_m_2.png", "char_m_3.png")
        self.char_img_w = ("char_w_1.png", "char_w_2.png", "char_w_3.png")

        self.init_lineedit()
        self.init_display_char()
        self.init_button()

        self.setCentralWidget(self.centralwidget)

        self.show()

    def init_display_char(self):
        self.char = QLabel(self.centralwidget)
        self.char.setGeometry(QRect(300, 50, 841, 720))
        if self.sex == 0:
            self.char.setPixmap(QPixmap(f"img/char/{self.char_img_m[0]}"))
        else:
            self.char.setPixmap(QPixmap(f"img/char/{self.char_img_w[0]}"))

        self.char.setScaledContents(True)

    def init_lineedit(self):
        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Please Enter Your player name")
        self.name.setGeometry(680, 810, 140, 30)

    def init_button(self):
        self.btn_switch_previous = ui.PicButton(QPixmap("img/char/arrow_1.png"),
                                                QPixmap(
                                                    "img/char/arrow_1.1.png"),
                                                QPixmap("img/char/arrow_1.2.png"), self.centralwidget)
        self.btn_switch_previous.move(400, 500)
        self.btn_switch_previous.clicked.connect(lambda: self.switch(1))

        self.btn_switch_next = ui.PicButton(QPixmap("img/char/arrow_2.png"),
                                            QPixmap("img/char/arrow_2.1.png"),
                                            QPixmap("img/char/arrow_2.2.png"), self.centralwidget)
        self.btn_switch_next.move(1100, 500)
        self.btn_switch_next.clicked.connect(lambda: self.switch(-1))

        self.btn_create = QPushButton("Create", self)
        self.btn_create.move(700, 845)
        self.btn_create.clicked.connect(self.create)

        self.btn_sex = QPushButton("Change sex", self)
        self.btn_sex.move(100, 300)
        self.btn_sex.clicked.connect(self.change_sex)

    def change_sex(self):
        if self.sex == 0:
            self.sex = 1
            self.char.setPixmap(QPixmap(f"img/char/{self.char_img_w[0]}"))
        else:
            self.sex = 0
            self.char.setPixmap(QPixmap(f"img/char/{self.char_img_m[0]}"))

    def create(self):
        name = self.name.text()
        if len(name) > 12 or len(name) < 4:
            QMessageBox.about(self, "Create_player",
                              "Your name must be between 5 and 12 characters.")
        else:
            myDataBase = Database(constinfo.mysql_config)
            myDataBase.connect()
            table = 'player'
            query = constinfo.SQL_INSERT.format(
                columns=','.join(constinfo.columns_create_player), table=table,
                placeholders=','.join(['%s' for i in range(
                    len(constinfo.columns_create_player))])
            )
            myDataBase.post(query, (constinfo.account_id, name, 1))

            self.close()
            self.next = uimainmenu.WindowMainMenu()

    def switch(self, nextt):
        if self.sex == 0:
            new_char = self.char_img_m[(
                self.curr_char + nextt) % len(self.char_img_m)]
        else:
            new_char = self.char_img_w[(
                self.curr_char + nextt) % len(self.char_img_w)]
        self.display_char(new_char)
        self.curr_char += nextt

    def display_char(self, path):
        self.char.setPixmap(QPixmap(f"img/char/{path}"))
