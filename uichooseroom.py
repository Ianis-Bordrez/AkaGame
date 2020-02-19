from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

from database import Database
import constinfo
import uigame
import ui


class WindowChooseRoom(ui.Window):
    def __init__(self):
        ui.Window.__init__(self, "AkaGame | Choose game")
        self.init_window()
        self.init_background("img/bckg_create_char.jpg")
        self.init_button()
        self.init_lineedit()
        self.show()

    def init_lineedit(self):
        self.room = QLineEdit(self)
        self.room.setPlaceholderText("Please Enter The Room Number")
        self.room.setGeometry(800, 200, 260, 30)
        self.room.setStyleSheet("color : black; border : 1px solid black; border-radius: 5px; font-size : 17px")
        self.room.setAlignment(Qt.AlignCenter)
        self.room.setMaxLength(6)

    def init_button(self):
        self.btn_french = QPushButton("French", self)
        self.btn_french.resize(150, 60)
        self.btn_french.move(400, 200)
        self.btn_french.setStyleSheet(
            "QPushButton { background-color: transparent; font-size: 20px; border : 2px solid black; border-radius : 20px }"
            "QPushButton:hover { background-color: rgba(50, 50, 50, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }"
            "QPushButton:pressed { background-color: rgba(250, 250, 250, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }"
        )
        self.btn_french.clicked.connect(self.start_game)

        self.btn_maths = QPushButton("Maths", self)
        self.btn_maths.resize(150, 60)
        self.btn_maths.move(400, 300)
        self.btn_maths.setStyleSheet(
            "QPushButton { background-color: transparent; font-size: 20px; border : 2px solid black; border-radius : 20px }"
            "QPushButton:hover { background-color: rgba(50, 50, 50, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }"
            "QPushButton:pressed { background-color: rgba(250, 250, 250, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }"
        )
        self.btn_maths.clicked.connect(lambda: self.start_game("maths"))

        self.btn_history = QPushButton("History", self)
        self.btn_history.resize(150, 60)
        self.btn_history.move(400, 400)
        self.btn_history.setStyleSheet(
            "QPushButton { background-color: transparent; font-size: 20px; border : 2px solid black; border-radius : 20px }"
            "QPushButton:hover { background-color: rgba(50, 50, 50, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }"
            "QPushButton:pressed { background-color: rgba(250, 250, 250, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }"
        )
        self.btn_history.clicked.connect(lambda: self.start_game("history"))

    def start_game(self, subject):
        quiz_id = self.room.text()
        if self.check_game(subject, quiz_id, room):
            self.close()
            self.next = uigame.WindowGame(subject, quiz_id)

    def check_game(self, subject, quiz_id, room):
        if room != 6:
            return False
        myDataBase = Database(constinfo.mysql_config)
        myDataBase.connect()

        query = f"SELECT * FROM quiz WHERE quiz_number='{quiz_id}' AND subject='{subject}'"
        res = myDataBase.get(query)
        if res:
            return True
        return False
