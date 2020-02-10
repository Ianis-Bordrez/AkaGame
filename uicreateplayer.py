from PyQt5.QtWidgets import QLineEdit, QPushButton, QLabel, QWidget
from PyQt5.QtGui import QPixmap
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

        self.init_lineedit()
        self.init_button()
        self.init_display_char()

        self.curr_char = 0
        self.char_img = ("char_m_1.png", "char_m_2.png", "char_m_3.png")

        self.setCentralWidget(self.centralwidget)

        self.show()

    def init_display_char(self):
        self.char = QLabel(self.centralwidget)
        self.char.setGeometry(QRect(200, 200, 841, 511))
        self.char.setPixmap(QPixmap("img/char/char_m_1.png"))
        self.char.setScaledContents(True)

    def init_lineedit(self):
        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Please Enter Your player name")
        self.name.setGeometry(580, 810, 140, 30)

    def init_button(self):
        self.btn_switch_char = QPushButton("Switch", self.centralwidget)
        self.btn_switch_char.move(100, 100)
        self.btn_switch_char.clicked.connect(self.switch)

        self.btn_create = QPushButton("Create", self)
        self.btn_create.move(600, 845)
        self.btn_create.clicked.connect(self.create)

    def create(self):
        name = self.name.text()
        if len(name) > 12 and len(name) < 4:
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

            self.next = uimainmenu.WindowMainMenu()

    def switch(self):
        new_char = self.char_img[(self.curr_char + 1) % len(self.char_img)]
        self.display_char(new_char)
        self.curr_char += 1

    def display_char(self, path):
        self.char.setPixmap(QPixmap(f"img/char/{path}"))
