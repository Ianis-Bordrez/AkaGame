from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import (
    QMainWindow,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QLabel,
)
from PyQt5.QtCore import Qt
from database import Database
import constinfo
import ui


class WindowCreateQuiz(ui.Window):
    def __init__(self):
        ui.Window.__init__(self, "Akagame | Create Quiz")
        self.init_window()
        self.init_background("img/imgbckg.jpg")
        self.init_lineedit()
        self.init_button()
        self.show()

    def init_lineedit(self):
        self.quiz_name = QLineEdit(self)
        self.quiz_name.setPlaceholderText("Please Enter Your quiz name")
        self.quiz_name.setGeometry(20, 100, 1200, 30)
        self.quiz_name.setStyleSheet(
            "background-color : transparent; color : black; border : 1px solid black; border-radius: 5px; font-size : 17px"
        )
        self.quiz_name.setAlignment(Qt.AlignCenter)

        self.question = QLineEdit(self)
        self.question.setPlaceholderText("Please Enter Your question")
        self.question.setGeometry(20, 200, 1200, 30)
        self.question.setStyleSheet(
            "background-color : transparent; color : black; border : 1px solid black; border-radius: 5px; font-size : 17px"
        )
        self.question.setAlignment(Qt.AlignCenter)

        self.answ_true = QLineEdit(self)
        self.answ_true.setPlaceholderText("Please Enter answer 1 (Correct answer)")
        self.answ_true.setGeometry(20, 270, 1200, 30)
        self.answ_true.setStyleSheet(
            "background-color : transparent; color : black; border : 1px solid black; border-radius: 5px; font-size : 17px"
        )
        self.answ_true.setAlignment(Qt.AlignCenter)

        self.answ2 = QLineEdit(self)
        self.answ2.setPlaceholderText("Please Enter answer 2")
        self.answ2.setGeometry(20, 340, 1200, 30)
        self.answ2.setStyleSheet(
            "background-color : transparent; color : black; border : 1px solid black; border-radius: 5px; font-size : 17px"
        )
        self.answ2.setAlignment(Qt.AlignCenter)

        self.answ3 = QLineEdit(self)
        self.answ3.setPlaceholderText("Please Enter answer 3")
        self.answ3.setGeometry(20, 420, 1200, 30)
        self.answ3.setStyleSheet(
            "background-color : transparent; color : black; border : 1px solid black; border-radius: 5px; font-size : 17px"
        )
        self.answ3.setAlignment(Qt.AlignCenter)

        self.answ4 = QLineEdit(self)
        self.answ4.setPlaceholderText("Please Enter answer 4")
        self.answ4.setGeometry(20, 500, 1200, 30)
        self.answ4.setStyleSheet(
            "background-color : transparent; color : black; border : 1px solid black; border-radius: 5px; font-size : 17px"
        )
        self.answ4.setAlignment(Qt.AlignCenter)

    def init_button(self):
        self.btn_create = QPushButton("Create", self)
        self.btn_create.resize(150, 60)
        self.btn_create.move(565, 600)
        self.btn_create.clicked.connect(self.create_quiz)
        self.btn_create.setStyleSheet(
            "QPushButton { background-color: transparent; font-size: 20px; border : 2px solid black; border-radius : 20px }"
            "QPushButton:hover { background-color: rgba(50, 50, 50, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }"
            "QPushButton:pressed { background-color: rgba(250, 250, 250, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }"
        )

        self.btn_cancel = QPushButton("cancel", self)
        self.btn_cancel.resize(150, 60)
        self.btn_cancel.move(565, 670)
        self.btn_cancel.clicked.connect(self.cancel)
        self.btn_cancel.setStyleSheet(
            "QPushButton { background-color: transparent; font-size: 20px; border : 2px solid black; border-radius : 20px }"
            "QPushButton:hover { background-color: rgba(50, 50, 50, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }"
            "QPushButton:pressed { background-color: rgba(250, 250, 250, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }"
        )

    def cancel(self):
        self.close()
        # self.next =

    def create_quiz(self):
        quiz_name = self.quiz_name.text()
        question = self.question.text()
        answ_true = self.answ_true.text()
        answ2 = self.answ2.text()
        answ3 = self.answ3.text()
        answ4 = self.answ4.text()
        quiz_number = None

        if self.check_quiz(question, answ_true, answ2, answ3, answ4):
            myDataBase = Database(constinfo.mysql_config)
            myDataBase.connect()
            print(quiz_name)

            quiz_number = myDataBase.get(f"SELECT quiz_id FROM quiz WHERE name='{quiz_name}'")

            if not quiz_number:

                quiz_number = self.generate_quiz_number()

                while myDataBase.get(f"SELECT quiz_id FROM quiz WHERE quiz_id='{quiz_number}'"):
                    quiz_number = self.generate_quiz_number()

                constinfo.teatcher_subject = "MATHS"

                table = "quiz"
                query = constinfo.SQL_INSERT.format(
                    columns=",".join(constinfo.columns_create_quiz),
                    table=table,
                    placeholders=",".join(["%s" for i in range(len(constinfo.columns_create_quiz))]),
                )
                myDataBase.post(
                    query, (quiz_number, constinfo.teatcher_subject, quiz_name,),
                )
            else:
                quiz_number = quiz_number[0]

            table = "quiz_question"
            query = constinfo.SQL_INSERT.format(
                columns=",".join(constinfo.columns_create_question),
                table=table,
                placeholders=",".join(["%s" for i in range(len(constinfo.columns_create_question))]),
            )
            myDataBase.post(query, (quiz_number, question, answ_true, answ2, answ3, answ4))

    def quiz_exist(self, database, name):
        database.get(f"SELECT name FROM quiz WHERE name='{name}'")

    def check_quiz(self, question, answ_true, answ2, answ3, answ4):
        if question == "" or answ_true == "" or answ2 == "" or answ3 == "" or answ4 == "":
            print("Veuillez remplir tous les champs")
            return False
        return True

    def generate_quiz_number(self):
        import string
        import random

        all_chars = string.ascii_letters + string.digits
        password = "".join(random.choice(all_chars) for x in range(6))
        return password
