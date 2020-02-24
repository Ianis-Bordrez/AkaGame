from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QWidget, QHBoxLayout, QGridLayout, QRadioButton, QLabel
from PyQt5.QtCore import Qt, QRect
from PyQt5 import QtCore
from database import Database
import constinfo
import ui
import random
import uimainmenu


class WindowGame(ui.Window):
    def __init__(self, subject, quiz_id):
        ui.Window.__init__(self, "AkaGame | Game")
        self.init_window()
        self.init_background("img/bckg_create_char.jpg")
        self.init_title("Quiz")
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.quiz_id = quiz_id
        self.curr_question = 0
        self.subject = subject
        self.answer1 = None
        self.answer2 = None
        self.answer3 = None
        self.answer4 = None

        self.true_answer = 0

        self.true_answer_count = 0
        self.false_answer_count = 0

        self.myDataBase = Database(constinfo.mysql_config)
        self.myDataBase.connect()
        self.res = self.myDataBase.get(
            f"SELECT answer_true,answer_2,answer_3,answer_4 FROM quiz_question WHERE quiz_id='{self.quiz_id}'"
        )
        self.total_question = len(self.res)
        self.answ_grid = QGridLayout(self.centralwidget)
        self.answ_grid.setAlignment(Qt.AlignCenter)
        # self.setLayout(self.answ_grid)
        self.init_answer(self.curr_question)
        self.btn_verif = QPushButton("Verif", self.centralwidget)
        self.answ_grid.addWidget(self.btn_verif, 2, 1, 1, 2)
        self.btn_verif.clicked.connect(self.verif_question)

        self.show()

    def init_answer(self, curr_question):
        question_number = (0, 1, 2, 3)
        rand = random.sample(range(0, 4), 4)
        while rand[self.true_answer] != 0:
            self.true_answer += 1

        self.answer1 = QRadioButton(self.res[curr_question][question_number[rand[0]]])
        self.answer2 = QRadioButton(self.res[curr_question][question_number[rand[1]]])
        self.answer3 = QRadioButton(self.res[curr_question][question_number[rand[2]]])
        self.answer4 = QRadioButton(self.res[curr_question][question_number[rand[3]]])
        self.answer1.setStyleSheet("QRadioButton { font: bold 14px; }")
        self.answer2.setStyleSheet("QRadioButton { font: bold 14px; }")
        self.answer3.setStyleSheet("QRadioButton { font: bold 14px; }")
        self.answer4.setStyleSheet("QRadioButton { font: bold 14px; }")
        self.answ_grid.addWidget(self.answer1, 1, 0)
        self.answ_grid.addWidget(self.answer2, 1, 1)
        self.answ_grid.addWidget(self.answer3, 1, 2)
        self.answ_grid.addWidget(self.answer4, 1, 3)

    def verif_question(self):
        if self.true_answer == 0:
            if self.answer1.isChecked():
                self.true_answer_count += 1
            else:
                self.false_answer_count += 1
        elif self.true_answer == 1:
            if self.answer2.isChecked():
                self.true_answer_count += 1
            else:
                self.false_answer_count += 1
        elif self.true_answer == 2:
            if self.answer3.isChecked():
                self.true_answer_count += 1
            else:
                self.false_answer_count += 1
        elif self.true_answer == 3:
            if self.answer4.isChecked():
                self.true_answer_count += 1
            else:
                self.false_answer_count += 1

        self.curr_question += 1

        if self.curr_question == self.total_question:
            table = "marks"
            query = constinfo.SQL_INSERT.format(
                columns=",".join(constinfo.columns_create_marks),
                table=table,
                placeholders=",".join(["%s" for i in range(len(constinfo.columns_create_marks))]),
            )
            self.myDataBase.post(
                query,
                (constinfo.account_id, self.subject, self.quiz_id, self.true_answer_count * 20 / self.total_question),
            )

            self.close()
            self.next = WindowEndGameStat(
                self.subject, self.true_answer_count, self.false_answer_count, self.total_question
            )
        else:
            self.new_question(self.curr_question)

    def new_question(self, question):
        self.true_answer = 0
        question_number = (0, 1, 2, 3)
        rand = random.sample(range(0, 4), 4)
        while rand[self.true_answer] != 0:
            self.true_answer += 1

        self.answer1.setText(self.res[question][question_number[rand[0]]])
        self.answer2.setText(self.res[question][question_number[rand[1]]])
        self.answer3.setText(self.res[question][question_number[rand[2]]])
        self.answer4.setText(self.res[question][question_number[rand[3]]])


class WindowEndGameStat(ui.Window):
    def __init__(self, subject, true_answer, false_answer, total_question):
        ui.Window.__init__(self, "AkaGame | Game")
        self.init_window()
        self.init_background("img/bckg_create_char.jpg")

        self.wdg_answer = QWidget(self.centralwidget)
        self.wdg_answer.setGeometry(100, 100, 300, 200)

        self.subject = subject
        self.true_answer = true_answer
        self.false_answer = false_answer
        self.total_question = total_question

        self.btn_return = ui.ReturnButton(uimainmenu.WindowMainMenu, self.close, parent=self.centralwidget)

        self.init_answer()

        self.show()

    def init_answer(self):
        self.lbl_true_answer = QLabel(self.wdg_answer)
        self.lbl_true_answer.setGeometry(440, 230, 400, 30)
        self.lbl_true_answer.setText(f"Réponses justes : {self.true_answer}")
        self.lbl_true_answer.setStyleSheet("color: green; text-align : center")
        self.lbl_true_answer.move(0, 0)

        self.lbl_false_answer = QLabel(self.wdg_answer)
        self.lbl_false_answer.setGeometry(440, 250, 400, 30)
        self.lbl_false_answer.setText(f"Réponses fausses : {self.false_answer}")
        self.lbl_false_answer.setStyleSheet("color: red; text-align : center")
        self.lbl_false_answer.move(0, 15)

        self.lbl_false_answer = QLabel(self.wdg_answer)
        self.lbl_false_answer.setGeometry(440, 270, 400, 30)
        self.lbl_false_answer.setText(f"Note finale : {self.true_answer} / {self.total_question}")
        self.lbl_false_answer.setStyleSheet("color: blue; text-align : center")
        self.lbl_false_answer.move(0, 30)

    def return_login(self):
        self.close()
        self.next = uimainmenu.WindowMainMenu()


from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    App = QApplication(sys.argv)
    p = WindowGame("MATHS", "M4eyU2")
    p.show()
    sys.exit(App.exec())
