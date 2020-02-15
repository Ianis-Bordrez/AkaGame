from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton
from database import Database
import constinfo
import ui


class WindowChooseSubject(ui.Window):
    def __init__(self):
        ui.Window.__init__(self, "AkaGame | Choose subject")
        self.init_window()
        self.init_background("img/bckg_create_char.jpg")
        self.init_button()
        self.show()

    def init_button(self):
        self.btn_french = QPushButton("French", self)
        self.btn_french.resize(150, 60)
        self.btn_french.move(600, 200)
        self.btn_french.setStyleSheet("QPushButton { background-color: transparent; font-size: 20px; border : 2px solid black; border-radius : 20px }"
                                      "QPushButton:hover { background-color: rgba(50, 50, 50, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }"
                                      "QPushButton:pressed { background-color: rgba(250, 250, 250, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }")
        self.btn_french.clicked.connect(self.choose_subject)

        self.btn_maths = QPushButton("Maths", self)
        self.btn_maths.resize(150, 60)
        self.btn_maths.move(600, 300)
        self.btn_maths.setStyleSheet("QPushButton { background-color: transparent; font-size: 20px; border : 2px solid black; border-radius : 20px }"
                                     "QPushButton:hover { background-color: rgba(50, 50, 50, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }"
                                     "QPushButton:pressed { background-color: rgba(250, 250, 250, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }")
        self.btn_maths.clicked.connect(lambda: self.choose_subject("maths"))

        self.btn_history = QPushButton("History", self)
        self.btn_history.resize(150, 60)
        self.btn_history.move(600, 400)
        self.btn_history.setStyleSheet("QPushButton { background-color: transparent; font-size: 20px; border : 2px solid black; border-radius : 20px }"
                                       "QPushButton:hover { background-color: rgba(50, 50, 50, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }"
                                       "QPushButton:pressed { background-color: rgba(250, 250, 250, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }")
        self.btn_history.clicked.connect(
            lambda: self.choose_subject("history"))

    def choose_subject(self, subject):
        if subject == "history":
            print(0)
        elif subject == "maths":
            print(2)
