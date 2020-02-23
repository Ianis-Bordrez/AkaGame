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
        self.qTimer.setInterval(500)
        self.qTimer.timeout.connect(self.update_data)
        self.qTimer.start()

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.test = QHBoxLayout(self.centralwidget)

        self.init_quiz()
        self.init_question()

        self.show()

    def update_data(self):
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

    def init_quiz(self):
        self.quiz_manager_grpbox = QGroupBox("Créer/suprimer un quiz", self.centralwidget)
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
        self.quiz_manager_lbl_name2.setText("Nom")

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
        self.test.addWidget(self.quiz_manager_grpbox)

    def init_question(self):
        self.question_manager_grpbox2 = QGroupBox("Créer/suprimer une question", self.centralwidget)
        self.question_manager = QFormLayout()

        self.question_manager_lbl_quiz_list = QLabel()
        self.question_manager_lbl_quiz_list.setText("Quiz")
        self.question_manager_scroll_quiz_list = QComboBox()

        quiz_list = self.myDataBase.get("SELECT DISTINCT quiz_id,subject,name FROM quiz")
        for quiz in quiz_list:
            self.question_manager_scroll_quiz_list.addItem(quiz[2])

        self.question_manager_lbl_action = QLabel()
        self.question_manager_lbl_action.setText("Action")
        self.question_manager_scroll_action = QComboBox()
        self.question_manager_scroll_action.addItem("Créer")
        self.question_manager_scroll_action.addItem("Supprimer")

        self.question_manager_lbl_question = QLabel()
        self.question_manager_lbl_question.setText("Question")
        self.question_manager_lineedit_question = QLineEdit()

        self.question_manager_lbl_true_answer = QLabel()
        self.question_manager_lbl_true_answer.setText("Nom")
        self.question_manager_lineedit_true_answer = QLineEdit()

        self.question_manager_list_quiz = QComboBox()

        quiz_list = self.myDataBase.get("SELECT DISTINCT quiz_id,subject,name FROM quiz")
        for quiz in quiz_list:
            self.question_manager_list_quiz.addItem(quiz[2])

        self.question_manager_validate = QPushButton("Valider")

        self.question_manager.addRow(self.quiz_manager_lbl_action, self.quiz_manager_scroll_action)
        self.question_manager.addRow(self.quiz_manager_lbl_name, self.quiz_manager_lineedit_name)
        self.question_manager.addRow(self.quiz_manager_lbl_name2, self.quiz_manager_list_quiz)
        self.question_manager.addRow(self.quiz_manager_validate)

        self.question_manager_grpbox2.setLayout(self.quiz_manager)
        self.test.addWidget(self.quiz_manager_grpbox2)


from PyQt5.QtWidgets import QApplication
import sys
from uilogin import WindowLogin


if __name__ == "__main__":
    App = QApplication(sys.argv)
    Window = WindowCreateQuiz()
    sys.exit(App.exec())
