from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QComboBox, QLabel
from PyQt5.QtCore import Qt

from database import Database
import constinfo
import uigame
import ui


class WindowChooseRoom(ui.Window):
    def __init__(self):
        ui.Window.__init__(self, "AkaGame | Choose game")
        self.init_window()
        self.init_background("img/bckg_create_char.jpg")
        self.init_subject()
        self.init_lineedit()
        self.init_button()
        self.init_error_lbl()
        self.show()

    def init_lineedit(self):
        self.room = QLineEdit(self)
        self.room.setPlaceholderText("Please Enter The Room Number")
        self.room.setGeometry(800, 200, 260, 30)
        self.room.setStyleSheet("color : black; border : 1px solid black; border-radius: 5px; font-size : 17px")
        self.room.setAlignment(Qt.AlignCenter)
        self.room.setMaxLength(6)

    def init_subject(self):

        subject = self.myDataBase.get("SELECT DISTINCT id,subject FROM quiz")

        self.scroll_subject_choose = QComboBox(self)
        self.scroll_subject_choose.setGeometry(590, 535, 100, 30)
        self.scroll_subject_choose.setStyleSheet(
            "QComboBox {  border-radius: 3px; }" "QComboBox QAbstractItemView {  border-radius: 3px; }"
        )
        if subject is None:
            self.scroll_subject_choose.addItem("Aucun quiz")
            return False
        for sub in subject:
            self.scroll_subject_choose.addItem(sub[1].pop())

    def init_button(self):
        self.btn_join_room = QPushButton("Create", self)
        self.btn_join_room.resize(150, 60)
        self.btn_join_room.move(565, 400)
        self.btn_join_room.clicked.connect(self.join_room)
        self.btn_join_room.setStyleSheet(
            "QPushButton { background-color: transparent; font-size: 20px; border : 2px solid black; border-radius : 20px }"
            "QPushButton:hover { background-color: rgba(50, 50, 50, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }"
            "QPushButton:pressed { background-color: rgba(250, 250, 250, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px }"
        )

    def init_error_lbl(self):
        self.lbl_error = QLabel(self)
        self.lbl_error.setGeometry(440, 230, 400, 30)

    def join_room(self):
        subject = self.scroll_subject_choose.currentText()
        quiz_id = self.room.text()
        if self.check_game(subject, quiz_id):
            self.close()
            self.next = uigame.WindowGame(subject, quiz_id)

    def check_game(self, subject, quiz_id):
        if len(quiz_id) != 6:
            self.lbl_error.setText("Veuillez entrer 6 caractères.")
            return False

        query = f"SELECT * FROM quiz WHERE quiz_id='{quiz_id}' AND subject='{subject}'"
        res = self.myDataBase.get(query)
        if res:
            query = f"SELECT * FROM marks WHERE quiz_id='{quiz_id}' AND subject='{subject}' AND account_id='{constinfo.account_id}'"
            res = self.myDataBase.get(query)
            if res:
                print("1")
                self.lbl_error.setText("Vous avez déjà fait le quiz.")
            else:
                return True
        else:
            print("2")
            self.lbl_error.setText("Le quiz n'existe pas.")
        return False
