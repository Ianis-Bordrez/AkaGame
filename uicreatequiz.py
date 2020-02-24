from PyQt5.QtWidgets import (
    QWidget,
    QComboBox,
    QLineEdit,
    QPushButton,
    QLabel,
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
)
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
        self.init_title("Gestion des quiz")

        self.qTimer = QTimer()
        self.qTimer.setInterval(200)
        self.qTimer.timeout.connect(self.update_data)
        self.qTimer.start()

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.horizontal_box = QGridLayout(self.centralwidget)

        self.question_list = None
        self.current_quiz_name = None
        self.current_quiz_id = None
        self.id_quiz_current_name = None

        self.question_has_been_create = None

        self.init_quiz()
        self.init_question()
        self.init_quiz_get_id()

        self.btn_return = ui.ReturnButton(uimainmenuteatcher.WindowTeatcher, self.close, parent=self.centralwidget)

        self.show()

    def update_data(self, force_update=False):
        if self.quiz_manager_scroll_action.currentText() == "Créer":
            self.quiz_manager_lbl_name.show()
            self.quiz_manager_lbl_name2.hide()
            self.quiz_manager_lineedit_name.show()
            self.quiz_manager_scroll_quiz.hide()
        else:
            self.quiz_manager_lbl_name.hide()
            self.quiz_manager_lbl_name2.show()
            self.quiz_manager_lineedit_name.hide()
            self.quiz_manager_scroll_quiz.show()

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
                if self.current_quiz_name:
                    self.current_quiz_id = self.myDataBase.get(
                        f"SELECT quiz_id FROM quiz WHERE name='{self.current_quiz_name}'"
                    )[0]
                    question_list = self.myDataBase.get(
                        f"SELECT id,question FROM quiz_question WHERE quiz_id='{self.current_quiz_id}'"
                    )
                    if question_list:
                        for question in question_list:
                            self.question_manager_scroll_question.addItem(question[1])

        id_quiz_name = self.quiz_id_manager_scroll_quiz_list.currentText()
        if self.id_quiz_current_name != id_quiz_name:
            self.id_quiz_current_name = id_quiz_name
            if id_quiz_name:
                current_quiz_id = self.myDataBase.get(f"SELECT quiz_id FROM quiz WHERE name='{id_quiz_name}'")[0]
                self.quiz_id_manager_lbl_quiz_id.setText(current_quiz_id)

        if force_update:
            self.question_manager_scroll_quiz_list.clear()
            self.quiz_manager_scroll_quiz.clear()
            quiz_list = self.myDataBase.get(
                f"SELECT quiz_id,name FROM quiz WHERE subject='{constinfo.teatcher_subject}'"
            )
            if quiz_list:
                for quiz in quiz_list:
                    self.question_manager_scroll_quiz_list.addItem(quiz[1])
                    self.quiz_manager_scroll_quiz.addItem(quiz[1])

    # ========================================
    # ===========QUIZ MANAGER=================
    # ========================================

    def init_quiz(self):
        self.quiz_manager_grpbox = QGroupBox("Créer/suprimer un quiz", self.centralwidget)
        self.quiz_manager_grpbox.setMaximumSize(300, 130)
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

        self.quiz_manager_scroll_quiz = QComboBox()

        quiz_list = self.myDataBase.get(
            f"SELECT DISTINCT quiz_id,subject,name FROM quiz WHERE subject='{constinfo.teatcher_subject}'"
        )
        if quiz_list != None:
            for quiz in quiz_list:
                self.quiz_manager_scroll_quiz.addItem(quiz[2])

        self.quiz_manager_btn_validate = QPushButton("Valider")
        self.quiz_manager_btn_validate.clicked.connect(
            lambda: self.quiz_manager_validate(self.quiz_manager_scroll_action.currentText())
        )

        self.quiz_manager.addRow(self.quiz_manager_lbl_action, self.quiz_manager_scroll_action)
        self.quiz_manager.addRow(self.quiz_manager_lbl_name, self.quiz_manager_lineedit_name)
        self.quiz_manager.addRow(self.quiz_manager_lbl_name2, self.quiz_manager_scroll_quiz)
        self.quiz_manager.addRow(self.quiz_manager_btn_validate)

        self.quiz_manager_grpbox.setLayout(self.quiz_manager)
        self.horizontal_box.addWidget(self.quiz_manager_grpbox, 0, 0)

    def quiz_manager_validate(self, arg):
        if arg == "Créer":
            quiz_name = self.quiz_manager_lineedit_name.text()
            quiz_number = self.generate_quiz_number()

            if self.myDataBase.get(f"SELECT name FROM quiz WHERE name='{quiz_name}'"):
                self.quiz_manager_timer_validate("Le nom du quiz existe déjà !")
                return False
            elif quiz_name == "":
                self.quiz_manager_timer_validate("Le nom du quiz ne peut pas être vide !")
                return False

            while self.myDataBase.get(f"SELECT quiz_id,name FROM quiz WHERE quiz_id='{quiz_number}'"):
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
            self.quiz_manager_lineedit_name.clear()
            self.quiz_manager_timer_validate("Quiz créer avec succès !")
        else:
            # fmt: off
            quiz_name = self.quiz_manager_scroll_quiz.currentText().replace("'", "\\'")
            # fmt: on
            if quiz_name:
                quiz_number = self.myDataBase.get(f"SELECT quiz_id FROM quiz WHERE name='{quiz_name}'")[0]
                self.myDataBase.post(f"DELETE FROM quiz WHERE quiz_id='{quiz_number}'")
                self.myDataBase.post(f"DELETE FROM quiz_question WHERE quiz_id='{quiz_number}'")
                self.quiz_manager_timer_validate("Quiz supprimé avec succès !")

                self.quiz_manager_scroll_quiz.clear()
                quiz_list = self.myDataBase.get("SELECT DISTINCT quiz_id,subject,name FROM quiz")
                for quiz in quiz_list:
                    self.quiz_manager_scroll_quiz.addItem(quiz[2])
            else:
                self.quiz_manager_timer_validate("Quiz supprimé avec succès !")

        self.update_data(force_update=True)

    def quiz_manager_timer_validate(self, sentence):
        self.validate_timer = QTimer()
        self.validate_timer.setInterval(5000)
        self.validate_timer.timeout.connect(lambda: self.quiz_manager_validate_timer_stop(sentence))
        self.validate_timer.start()

        self.quiz_manager_lbl_success = QLabel()
        self.quiz_manager_lbl_success.setText(sentence)
        self.quiz_manager.addRow(self.quiz_manager_lbl_success)

    def quiz_manager_validate_timer_stop(self, sentence):
        self.validate_timer.stop()
        self.quiz_manager.removeRow(self.quiz_manager_lbl_success)

    def generate_quiz_number(self):
        import string
        import random

        all_chars = string.ascii_letters + string.digits
        password = "".join(random.choice(all_chars) for x in range(6))
        return password

    # ========================================
    # =======QUESTION MANAGER=================
    # ========================================

    def init_question(self):
        self.question_manager_grpbox = QGroupBox("Créer/suprimer une question", self.centralwidget)
        self.question_manager_grpbox.setMaximumSize(700, 300)
        self.question_manager = QFormLayout()

        self.question_manager_lbl_quiz_list = QLabel()
        self.question_manager_lbl_quiz_list.setText("Quiz")
        self.question_manager_scroll_quiz_list = QComboBox()

        quiz_list = self.myDataBase.get(f"SELECT quiz_id,name FROM quiz WHERE subject='{constinfo.teatcher_subject}'")
        if quiz_list:
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
        self.horizontal_box.addWidget(self.question_manager_grpbox, 0, 1)

    def question_manager_validate(self, arg):
        quiz_name = self.question_manager_scroll_quiz_list.currentText()

        if arg == "Créer":
            quiz = self.question_manager_scroll_quiz_list.currentText()
            question = self.question_manager_lineedit_question.text()
            answ_true = self.question_manager_lineedit_true_answer.text()
            answ2 = self.question_manager_lineedit_answer2.text()
            answ3 = self.question_manager_lineedit_answer3.text()
            answ4 = self.question_manager_lineedit_answer4.text()

            if self.check_quiz(quiz, question, answ_true, answ2, answ3, answ4):

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
                self.question_manager_timer_validate("Question créée avec succès !")
                self.question_has_been_create = True
        else:
            # fmt: off
            question = self.question_manager_scroll_question.currentText().replace("'", "\\'")
            # fmt: on
            if question:
                quiz_number = self.myDataBase.get(f"SELECT quiz_id FROM quiz WHERE name='{quiz_name}'")[0]
                self.myDataBase.post(
                    f"DELETE FROM quiz_question WHERE question='{question}' AND quiz_id='{quiz_number}'"
                )
                self.update_data(force_update=True)
                self.question_manager_timer_validate("Question supprimée avec succès !")
            else:
                self.question_manager_timer_validate("Aucune question à supprimer !")

    def check_quiz(self, quiz, question, answ_true, answ2, answ3, answ4):
        if quiz == "" or question == "" or answ_true == "" or answ2 == "" or answ3 == "" or answ4 == "":
            self.question_manager_timer_validate("Veuillez remplir tous les champs !")
            return False
        return True

    def question_manager_timer_validate(self, sentence):
        self.validate_timer = QTimer()
        self.validate_timer.setInterval(5000)
        self.validate_timer.timeout.connect(lambda: self.question_manager_timer_stop(sentence))
        self.validate_timer.start()

        self.question_manager_lbl_success = QLabel()
        self.question_manager_lbl_success.setText(sentence)
        self.question_manager.addRow(self.question_manager_lbl_success)

    def question_manager_timer_stop(self, sentence):
        self.validate_timer.stop()
        self.question_manager.removeRow(self.question_manager_lbl_success)

    # ========================================
    # ===============QUIZ ID==================
    # ========================================

    def init_quiz_get_id(self):
        self.quiz_id_manager_grpbox = QGroupBox("Récupérer l'ID du quiz", self.centralwidget)
        self.quiz_id_manager_grpbox.setMaximumSize(200, 80)
        self.quiz_id_manager = QFormLayout()

        self.quiz_id_manager_lbl_quiz_list = QLabel()
        self.quiz_id_manager_lbl_quiz_list.setText("Quiz")

        self.quiz_id_manager_scroll_quiz_list = QComboBox()

        quiz_list = self.myDataBase.get(f"SELECT quiz_id,name FROM quiz WHERE subject='{constinfo.teatcher_subject}'")
        if quiz_list:
            for quiz in quiz_list:
                self.quiz_id_manager_scroll_quiz_list.addItem(quiz[1])

        self.quiz_id_manager_lbl_id = QLabel()
        self.quiz_id_manager_lbl_id.setText("ID")

        self.quiz_id_manager_lbl_quiz_id = QLabel()
        self.quiz_id_manager_lbl_quiz_id.setText("")

        self.quiz_id_manager.addRow(self.quiz_id_manager_lbl_quiz_list, self.quiz_id_manager_scroll_quiz_list)
        self.quiz_id_manager.addRow(self.quiz_id_manager_lbl_id, self.quiz_id_manager_lbl_quiz_id)

        self.quiz_id_manager_grpbox.setLayout(self.quiz_id_manager)
        self.horizontal_box.addWidget(self.quiz_id_manager_grpbox, 1, 1)
