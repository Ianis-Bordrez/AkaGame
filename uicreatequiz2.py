from PyQt5.QtWidgets import QWidget, QComboBox, QLineEdit, QPushButton, QLabel, QFormLayout, QGroupBox, QHBoxLayout
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
        self.init_title("Création de quiz")

        self.qTimer = QTimer()
        self.qTimer.setInterval(200)
        self.qTimer.timeout.connect(self.update_data)
        self.qTimer.start()

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.horizontal_box = QHBoxLayout(self.centralwidget)

        self.question_list = None
        self.current_quiz_name = None
        self.current_quiz_id = None

        self.question_has_been_create = None

        self.init_quiz()
        self.init_question()

        self.show()

    def update_data(self, force_update=False):
        if self.quiz_manager_scroll_action.currentText() == "Créer":
            self.quiz_manager_lbl_name.show()
            self.quiz_manager_lbl_name2.hide()
            self.quiz_manager_lineedit_name.show()
            self.quiz_manager_list_quiz.hide()
        else:
            self.quiz_manager_lbl_name.hide()
            self.quiz_manager_lbl_name2.show()
            self.quiz_manager_lineedit_name.hide()
            self.quiz_manager_list_quiz.show()

        if self.question_manager_scroll_action.currentText() == "Créer":
            self.question_manager_lbl_question.show()
            self.question_manager_lineedit_question.show()
            self.question_manager_lbl_true_answer.show()
            self.question_manager_lineedit_true_answer.show()
            self.question_manager_lbl_answer2.show()
            self.question_manager_lineedit_answer2.show()
            self.question_manager_lbl_answer3.show()
            self.question_manager_lineedit_answer3.show()
            self.question_manager_lbl_answer4.show()
            self.question_manager_lineedit_answer4.show()
            self.question_manager_scroll_question.hide()
            self.question_manager_lbl_delete.hide()
        else:
            if self.question_has_been_create:
                force_update = True
                self.question_has_been_create = False
            self.question_manager_lbl_question.hide()
            self.question_manager_lineedit_question.hide()
            self.question_manager_lbl_true_answer.hide()
            self.question_manager_lineedit_true_answer.hide()
            self.question_manager_lbl_answer2.hide()
            self.question_manager_lineedit_answer2.hide()
            self.question_manager_lbl_answer3.hide()
            self.question_manager_lineedit_answer3.hide()
            self.question_manager_lbl_answer4.hide()
            self.question_manager_lineedit_answer4.hide()
            self.question_manager_scroll_question.show()
            self.question_manager_lbl_delete.show()
            quiz_name = self.question_manager_scroll_quiz_list.currentText()
            if not self.current_quiz_name == quiz_name or force_update:
                self.question_manager_scroll_question.clear()
                self.current_quiz_name = quiz_name
                self.current_quiz_id = self.myDataBase.get(
                    f"SELECT quiz_id FROM quiz WHERE name='{self.current_quiz_name}'"
                )[0]
                question_list = self.myDataBase.get(
                    f"SELECT id,question FROM quiz_question WHERE quiz_id='{self.current_quiz_id}'"
                )
                for question in question_list:
                    self.question_manager_scroll_question.addItem(question[1])

    def init_quiz(self):
        self.quiz_manager_grpbox = QGroupBox("Créer/suprimer un quiz", self.centralwidget)
        self.quiz_manager_grpbox.setMaximumSize(500, 500)
        self.quiz_manager = QFormLayout()

        self.quiz_manager_lbl_action = QLabel()
        self.quiz_manager_lbl_action.setText("Action")
        self.quiz_manager_scroll_action = QComboBox()
        self.quiz_manager_scroll_action.addItem("Créer")
        self.quiz_manager_scroll_action.addItem("Supprimer")

        self.quiz_manager_lbl_name = QLabel()
        self.quiz_manager_lbl_name.setText("Nom")
        self.quiz_manager_lineedit_name = QLineEdit()

        self.quiz_manager_lbl_name2 = QLabel()
        self.quiz_manager_lbl_name2.setText("Quiz")

        self.quiz_manager_list_quiz = QComboBox()

        quiz_list = self.myDataBase.get("SELECT DISTINCT quiz_id,subject,name FROM quiz")
        for quiz in quiz_list:
            self.quiz_manager_list_quiz.addItem(quiz[2])

        self.quiz_manager_validate = QPushButton("Valider")

        self.quiz_manager.addRow(self.quiz_manager_lbl_action, self.quiz_manager_scroll_action)
        self.quiz_manager.addRow(self.quiz_manager_lbl_name, self.quiz_manager_lineedit_name)
        self.quiz_manager.addRow(self.quiz_manager_lbl_name2, self.quiz_manager_list_quiz)
        self.quiz_manager.addRow(self.quiz_manager_validate)

        self.quiz_manager_grpbox.setLayout(self.quiz_manager)
        self.horizontal_box.addWidget(self.quiz_manager_grpbox)

    def init_question(self):
        self.question_manager_grpbox = QGroupBox("Créer/suprimer une question", self.centralwidget)
        self.question_manager_grpbox.setMaximumSize(500, 300)
        self.question_manager = QFormLayout()

        self.question_manager_lbl_quiz_list = QLabel()
        self.question_manager_lbl_quiz_list.setText("Quiz")
        self.question_manager_scroll_quiz_list = QComboBox()

        quiz_list = self.myDataBase.get("SELECT quiz_id,name FROM quiz")
        for quiz in quiz_list:
            self.question_manager_scroll_quiz_list.addItem(quiz[1])

        self.question_manager_lbl_action = QLabel()
        self.question_manager_lbl_action.setText("Action")
        self.question_manager_scroll_action = QComboBox()
        self.question_manager_scroll_action.addItem("Créer")
        self.question_manager_scroll_action.addItem("Supprimer")

        self.question_manager_lbl_question = QLabel()
        self.question_manager_lbl_question.setText("Question")
        self.question_manager_lineedit_question = QLineEdit()

        self.question_manager_lbl_true_answer = QLabel()
        self.question_manager_lbl_true_answer.setText("Réponse juste")
        self.question_manager_lineedit_true_answer = QLineEdit()

        self.question_manager_lbl_answer2 = QLabel()
        self.question_manager_lbl_answer2.setText("Réponse 2")
        self.question_manager_lineedit_answer2 = QLineEdit()

        self.question_manager_lbl_answer3 = QLabel()
        self.question_manager_lbl_answer3.setText("Réponse 3")
        self.question_manager_lineedit_answer3 = QLineEdit()

        self.question_manager_lbl_answer4 = QLabel()
        self.question_manager_lbl_answer4.setText("Réponse 4")
        self.question_manager_lineedit_answer4 = QLineEdit()

        self.question_manager_lbl_delete = QLabel()
        self.question_manager_lbl_delete.setText("Question")
        self.question_manager_scroll_question = QComboBox()

        self.question_manager_btn_validate = QPushButton("Valider")
        self.question_manager_btn_validate.clicked.connect(
            lambda: self.question_manager_validate(self.question_manager_scroll_action.currentText())
        )

        self.question_manager.addRow(self.question_manager_lbl_action, self.question_manager_scroll_action)
        self.question_manager.addRow(self.question_manager_lbl_quiz_list, self.question_manager_scroll_quiz_list)
        self.question_manager.addRow(self.question_manager_lbl_question, self.question_manager_lineedit_question)
        self.question_manager.addRow(self.question_manager_lbl_true_answer, self.question_manager_lineedit_true_answer)
        self.question_manager.addRow(self.question_manager_lbl_answer2, self.question_manager_lineedit_answer2)
        self.question_manager.addRow(self.question_manager_lbl_answer3, self.question_manager_lineedit_answer3)
        self.question_manager.addRow(self.question_manager_lbl_answer4, self.question_manager_lineedit_answer4)
        self.question_manager.addRow(self.question_manager_lbl_delete, self.question_manager_scroll_question)
        self.question_manager.addRow(self.question_manager_btn_validate)

        self.question_manager_grpbox.setLayout(self.question_manager)
        self.horizontal_box.addWidget(self.question_manager_grpbox)

    def question_manager_validate(self, arg):
        quiz_name = self.question_manager_scroll_quiz_list.currentText()

        if arg == "Créer":
            question = self.question_manager_lineedit_question.text()
            answ_true = self.question_manager_lineedit_true_answer.text()
            answ2 = self.question_manager_lineedit_answer2.text()
            answ3 = self.question_manager_lineedit_answer3.text()
            answ4 = self.question_manager_lineedit_answer4.text()

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

                self.question_manager_lineedit_question.clear()
                self.question_manager_lineedit_true_answer.clear()
                self.question_manager_lineedit_answer2.clear()
                self.question_manager_lineedit_answer3.clear()
                self.question_manager_lineedit_answer4.clear()
                self.question_manager_timer_validate_success("Question créée avec succès !")
                self.question_has_been_create = True
        else:
            # fmt: off
            question = self.question_manager_scroll_question.currentText().replace("'", "\\'")
            # fmt: on
            quiz_number = self.myDataBase.get(f"SELECT quiz_id FROM quiz WHERE name='{quiz_name}'")[0]
            self.myDataBase.post(f"DELETE FROM quiz_question WHERE question='{question}' AND quiz_id='{quiz_number}'")
            self.update_data(force_update=True)
            self.question_manager_timer_validate_success("Question supprimée avec succès !")

    def check_quiz(self, question, answ_true, answ2, answ3, answ4):
        if question == "" or answ_true == "" or answ2 == "" or answ3 == "" or answ4 == "":
            print("Veuillez remplir tous les champs")
            return False
        return True

    def question_manager_timer_validate_success(self, sentence):
        self.validate_timer = QTimer()
        self.validate_timer.setInterval(5000)
        self.validate_timer.timeout.connect(lambda: self.question_manager_validate_success(sentence))
        self.validate_timer.start()

        self.question_manager_lbl_success = QLabel()
        self.question_manager_lbl_success.setText(sentence)
        self.question_manager.addRow(self.question_manager_lbl_success)

    def question_manager_validate_success(self, sentence):
        self.validate_timer.stop()
        self.question_manager.removeRow(self.question_manager_lbl_success)


from PyQt5.QtWidgets import QApplication
import sys
from uilogin import WindowLogin


if __name__ == "__main__":
    App = QApplication(sys.argv)
    Window = WindowCreateQuiz()
    sys.exit(App.exec())
