from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton
from database import Database
import constinfo
import ui
import uicreatequiz


class WindowTeatcher(ui.Window):
    def __init__(self):
        ui.Window.__init__(self, "AkaGame | Teatcher main window")
        self.init_window()
        self.init_background("img/bckg_create_char.jpg")
        self.init_button()
        self.show()

    def init_button(self):
        self.btn_create_quiz = QPushButton("Create a quiz", self)
        self.btn_create_quiz.resize(150, 60)
        self.btn_create_quiz.move(525, 420)
        self.btn_create_quiz.setStyleSheet(
            "QPushButton { font-size: 20px; border : 2px solid black; border-radius : 20px }"
            "QPushButton:hover { background-color: rgba(50, 50, 50, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }"
            "QPushButton:pressed { background-color: rgba(250, 250, 250, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }"
        )
        self.btn_create_quiz.clicked.connect(self.create_quiz)

    def create_quiz(self):
        self.close()
        self.next = uicreatequiz.WindowCreateQuiz()
