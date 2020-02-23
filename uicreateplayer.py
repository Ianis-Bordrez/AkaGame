from PyQt5.QtWidgets import QLineEdit, QPushButton, QLabel, QWidget, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect
from database import Database
import uimainmenu
import constinfo
import ui
import uilogin


class WindowCreatePlayer(ui.Window):
    def __init__(self):
        ui.Window.__init__(self, "AkaGame | Create Player")
        self.init_window()
        self.init_background("img/bckg_create_char.jpg")

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.gender = 1
        self.curr_char = 0

        self.init_lineedit()
        self.init_display_char()
        self.init_button()

        self.btn_return = ui.ReturnButton(uilogin.WindowLogin, self.close, name="Annuler", parent=self.centralwidget)

        self.show()

    def init_display_char(self):
        self.char = QLabel(self.centralwidget)
        self.char.setGeometry(QRect(350, 180, 600, 600))
        if self.gender == 1:
            self.char.setPixmap(QPixmap(f"img/char/{constinfo.char_img_m[self.curr_char]}"))
        else:
            self.char.setPixmap(QPixmap(f"img/char/{constinfo.char_img_w[self.curr_char]}"))

        self.char.setScaledContents(True)

    def init_lineedit(self):
        self.name = QLineEdit(self.centralwidget)
        self.name.setPlaceholderText("Please Enter Your player name")
        self.name.setGeometry(520, 50, 240, 30)
        self.name.setStyleSheet(
            "background-color : transparent; color : black; border : 1px solid black; border-radius: 5px; font-size : 17px"
        )

    def init_button(self):
        self.btn_switch_previous = ui.PicButton(
            QPixmap("img/char/arrow_1.png"),
            QPixmap("img/char/arrow_1.1.png"),
            QPixmap("img/char/arrow_1.2.png"),
            self.centralwidget,
        )
        self.btn_switch_previous.move(250, 500)
        self.btn_switch_previous.clicked.connect(lambda: self.switch(-1))

        self.btn_switch_next = ui.PicButton(
            QPixmap("img/char/arrow_2.png"),
            QPixmap("img/char/arrow_2.1.png"),
            QPixmap("img/char/arrow_2.2.png"),
            self.centralwidget,
        )
        self.btn_switch_next.move(1000, 500)
        self.btn_switch_next.clicked.connect(lambda: self.switch(1))

        self.btn_create = QPushButton("Create", self)
        self.btn_create.move(565, 790)
        self.btn_create.resize(150, 60)
        self.btn_create.clicked.connect(self.create)
        self.btn_create.setStyleSheet(
            "QPushButton { background-color: transparent; font-size: 20px; border : 2px solid white; border-radius : 20px; color : white }"
            "QPushButton:hover { background-color: rgba(50, 50, 50, 0.5); font-size: 20px; border : 2px solid white; border-radius : 20px; color : white }"
            "QPushButton:pressed { background-color: rgba(250, 250, 250, 0.5); font-size: 20px; border : 2px solid white; border-radius : 20px; color : white }"
        )

        self.btn_sex = QPushButton("Change sex", self)
        self.btn_sex.move(565, 100)
        self.btn_sex.resize(150, 60)
        self.btn_sex.clicked.connect(self.change_sex)
        self.btn_sex.setStyleSheet(
            "QPushButton { background-color: transparent; font-size: 20px; border : 2px solid black; border-radius : 20px; }"
            "QPushButton:hover { background-color: rgba(50, 50, 50, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px; }"
            "QPushButton:pressed { background-color: rgba(250, 250, 250, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px; }"
        )

    def change_sex(self):
        if self.gender == 1:
            self.gender = 2
            self.char.setPixmap(QPixmap(f"img/char/{constinfo.char_img_w[0]}"))
        else:
            self.gender = 1
            self.char.setPixmap(QPixmap(f"img/char/{constinfo.char_img_m[0]}"))

    def create(self):
        name = self.name.text()
        if len(name) > 12 or len(name) < 4:
            QMessageBox.about(self, "Create_player", "Your name must be between 5 and 12 characters.")
        else:
            table = "player"
            query = constinfo.SQL_INSERT.format(
                columns=",".join(constinfo.columns_create_player),
                table=table,
                placeholders=",".join(["%s" for i in range(len(constinfo.columns_create_player))]),
            )
            self.myDataBase.post(query, (constinfo.account_id, name, constinfo.player_char, self.gender))

            self.close()
            self.next = uimainmenu.WindowMainMenu()

    def switch(self, nextt):
        if self.gender == 1:
            new_char = constinfo.char_img_m[(self.curr_char + nextt) % len(constinfo.char_img_m)]
        else:
            new_char = constinfo.char_img_w[(self.curr_char + nextt) % len(constinfo.char_img_w)]
        self.display_char(new_char)
        self.curr_char += nextt
        gen = "w"
        if self.gender == 1:
            gen = "m"
        constinfo.player_char = f"img/char/char_{gen}_{(self.curr_char + nextt-1) % len(constinfo.char_img_m)+1}.png"
        print(constinfo.player_char)

    def display_char(self, path):
        self.char.setPixmap(QPixmap(f"img/char/{path}"))
