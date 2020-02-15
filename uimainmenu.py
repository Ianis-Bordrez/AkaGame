from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton
from database import Database
import constinfo
import ui
import uichoosesubject


class WindowMainMenu(ui.Window):
    def __init__(self):
        ui.Window.__init__(self, "AkaGame | Main Menu")
        self.init_window()
        self.init_background("img/bckg_create_char.jpg")
        self.init_button()
        self.show()

    def init_button(self):
        self.btn_game = QPushButton("Start", self)
        self.btn_game.resize(150, 60)
        self.btn_game.move(50, 50)
        self.btn_game.setStyleSheet("QPushButton { font-size: 20px; border : 2px solid black; border-radius : 20px }"
                                    "QPushButton:hover { background-color: rgba(50, 50, 50, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }"
                                    "QPushButton:pressed { background-color: rgba(250, 250, 250, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }")
        self.btn_game.clicked.connect(
            self.start_game)

    def start_game(self):
        self.close()
        self.next = uichoosesubject.WindowChooseSubject()
