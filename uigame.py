from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QWidget, QHBoxLayout, QGridLayout, QCheckBox, QLabel
from PyQt5.QtCore import Qt, QRect

from database import Database
import constinfo
import ui


class WindowGame(ui.Window):
    def __init__(self, quiz_id):
        ui.Window.__init__(self, "AkaGame | Game")
        self.init_window()
        self.init_background("img/bckg_create_char.jpg")
        self.centralwidget = WindowAnswer(quiz_id)
        self.setCentralWidget(self.centralwidget)
        self.show()


class WindowAnswer(QWidget):
    def __init__(self, room_id):
        super().__init__()
        self.room_id = room_id
        self.curr_question = 0

        myDataBase = Database(constinfo.mysql_config)
        myDataBase.connect()
        self.res = myDataBase.get(
            f"SELECT answer_true,answer_2,answer_3,answer_4 FROM quiz_question WHERE quiz_id='{self.room_id}'"
        )

        self.answ_grid = QGridLayout()
        self.answ_grid.setAlignment(Qt.AlignCenter)
        self.setLayout(self.answ_grid)

        self.init_answer(self.curr_question)
        self.btn_verif = QPushButton("Verif", self)
        self.answ_grid.addWidget(self.btn_verif, 2, 1, 1, 2)
        self.btn_verif.clicked.connect(self.verif_question)

        self.answer1 = None
        self.answer2 = None
        self.answer3 = None
        self.answer4 = None

    def init_answer(self, curr_question):
        import random

        question_number = (0, 1, 2, 3)
        rand = random.sample(range(0, 4), 4)
        self.answer1 = QCheckBox(self.res[curr_question][question_number[rand[0]]])
        self.answer2 = QCheckBox(self.res[curr_question][question_number[rand[1]]])
        self.answer3 = QCheckBox(self.res[curr_question][question_number[rand[2]]])
        self.answer4 = QCheckBox(self.res[curr_question][question_number[rand[3]]])
        self.answer1.setStyleSheet("QCheckBox { font: bold 14px; }")
        self.answer2.setStyleSheet("QCheckBox { font: bold 14px; }")
        self.answer3.setStyleSheet("QCheckBox { font: bold 14px; }")
        self.answer4.setStyleSheet("QCheckBox { font: bold 14px; }")

        self.answ_grid.addWidget(self.answer1, 1, 0)
        self.answ_grid.addWidget(self.answer2, 1, 1)
        self.answ_grid.addWidget(self.answer3, 1, 2)
        self.answ_grid.addWidget(self.answer4, 1, 3)

    def init_button(self):
        self.btn_create = QPushButton("Create", self)
        self.btn_create.move(700, 845)
        self.btn_create.clicked.connect(self.create)

    def verif_question(self):
        pass


from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    App = QApplication(sys.argv)
    # Window = WindowGame(51654)
    p = WindowGame("M4eyU2")
    p.show()
    sys.exit(App.exec())
