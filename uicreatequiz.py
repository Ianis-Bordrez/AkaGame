from PyQt5.QtWidgets import QWidget, QComboBox, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt, QTimer
from database import Database
import constinfo
import ui
import uimainmenuteatcher


class WindowCreateQuiz(ui.Window):
    def __init__(self):
        ui.Window.__init__(self, "Akagame | Create Quiz")
        self.init_window()
        self.init_background("img/imgbckg.jpg")

        self.qTimer = QTimer()
        self.qTimer.setInterval(500)
        self.qTimer.timeout.connect(self.getcombobox_values)
        self.qTimer.start()

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.init_create_quiz()

        self.init_lineedit()
        self.init_button()

        self.btn_return = ui.ReturnButton(uimainmenuteatcher.WindowTeatcher, self.close, parent=self.centralwidget)

        self.show()

    def getcombobox_values(self):
        if self.scroll_quiz_choose.currentText() == "Créer un quiz":
            self.quiz_name.show()
        else:
            self.quiz_name.hide()

    def init_create_quiz(self):
        self.lbl_quiz_choose = QLabel(self.centralwidget)
        self.lbl_quiz_choose.setGeometry(330, 275, 150, 30)
        self.lbl_quiz_choose.setText("Choisissez un quiz")
        self.lbl_quiz_choose.setAlignment(Qt.AlignRight)
        self.lbl_quiz_choose.setStyleSheet("font-size : 17px;")

        self.scroll_quiz_choose = QComboBox(self.centralwidget)
        self.scroll_quiz_choose.setGeometry(30, 20, 250, 30)
        self.scroll_quiz_choose.setStyleSheet(
            "QComboBox {  border-radius: 3px; }" "QComboBox QAbstractItemView {  border-radius: 3px; text }"
        )

        self.quiz_name = QLineEdit(self.centralwidget)
        self.quiz_name.setPlaceholderText("Veuillez entrer le nom du quiz")
        self.quiz_name.setGeometry(300, 20, 300, 30)
        self.quiz_name.setStyleSheet(constinfo.stylesheet_lineedit)
        self.quiz_name.setAlignment(Qt.AlignCenter)

        quiz_list = self.myDataBase.get("SELECT DISTINCT quiz_id,subject,name FROM quiz")

        self.scroll_quiz_choose.addItem("Créer un quiz")
        for quiz in quiz_list:
            self.scroll_quiz_choose.addItem(quiz[2])

    def init_lineedit(self):
        self.question = QLineEdit(self.centralwidget)
        self.question.setPlaceholderText("Please Enter Your question")
        self.question.setGeometry(20, 200, 800, 30)
        self.question.setStyleSheet(constinfo.stylesheet_lineedit)
        self.question.setAlignment(Qt.AlignCenter)

        self.answ_true = QLineEdit(self.centralwidget)
        self.answ_true.setPlaceholderText("Please Enter answer 1 (Correct answer)")
        self.answ_true.setGeometry(20, 270, 800, 30)
        self.answ_true.setStyleSheet(constinfo.stylesheet_lineedit)
        self.answ_true.setAlignment(Qt.AlignCenter)

        self.answ2 = QLineEdit(self.centralwidget)
        self.answ2.setPlaceholderText("Please Enter answer 2")
        self.answ2.setGeometry(20, 340, 800, 30)
        self.answ2.setStyleSheet(constinfo.stylesheet_lineedit)
        self.answ2.setAlignment(Qt.AlignCenter)

        self.answ3 = QLineEdit(self.centralwidget)
        self.answ3.setPlaceholderText("Please Enter answer 3")
        self.answ3.setGeometry(20, 420, 800, 30)
        self.answ3.setStyleSheet(constinfo.stylesheet_lineedit)
        self.answ3.setAlignment(Qt.AlignCenter)

        self.answ4 = QLineEdit(self.centralwidget)
        self.answ4.setPlaceholderText("Please Enter answer 4")
        self.answ4.setGeometry(20, 500, 1200, 30)
        self.answ4.setStyleSheet(constinfo.stylesheet_lineedit)
        self.answ4.setAlignment(Qt.AlignCenter)

    def init_button(self):
        self.btn_create = QPushButton("Create", self.centralwidget)
        self.btn_create.resize(150, 60)
        self.btn_create.move(565, 600)
        self.btn_create.clicked.connect(self.create_quiz)
        self.btn_create.setStyleSheet(constinfo.stylesheet_main_button)

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

            quiz_number = self.myDataBase.get(f"SELECT quiz_id FROM quiz WHERE name='{quiz_name}'")

            if not quiz_number:

                quiz_number = self.generate_quiz_number()

                while self.myDataBase.get(f"SELECT quiz_id FROM quiz WHERE quiz_id='{quiz_number}'"):
                    quiz_number = self.generate_quiz_number()

                table = "quiz"
                query = constinfo.SQL_INSERT.format(
                    columns=",".join(constinfo.columns_create_quiz),
                    table=table,
                    placeholders=",".join(["%s" for i in range(len(constinfo.columns_create_quiz))]),
                )
                self.myDataBase.post(
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
            self.myDataBase.post(query, (quiz_number, question, answ_true, answ2, answ3, answ4))

            self.answ_true.clear()
            self.answ2.clear()
            self.answ3.clear()
            self.answ4.clear()

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

