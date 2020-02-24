from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QComboBox, QLabel, QWidget, QProgressBar
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPixmap
import constinfo
import uigame
import ui
import uimainmenu


class WindowChooseRoom(ui.Window):
    def __init__(self):
        ui.Window.__init__(self, "AkaGame | Choose game")
        self.init_window()
        self.init_background("img/bckg_create_char.jpg")
        self.init_title("Choix du quiz")

        self.centralwidget = QWidget(self)

        self.init_display_char()

        self.setCentralWidget(self.centralwidget)

        self.init_subject()
        self.init_lineedit()
        self.init_button()
        self.init_error_lbl()
        self.init_hp_bar()

        self.btn_return = ui.ReturnButton(uimainmenu.WindowMainMenu, self.close, parent=self.centralwidget)

        self.show()

    def init_hp_bar(self):
        self.hp_bar = QProgressBar(self.centralwidget)
        self.hp_bar.setGeometry(500, 150, 300, 30)
        self.hp_bar.setMaximum(100)
        query_curr_hp = self.myDataBase.get(f"SELECT HP FROM player WHERE account_id={constinfo.account_id}")
        self.hp_bar.setValue(query_curr_hp[0])
        self.hp_bar.setStyleSheet(
            "QProgressBar { border: 2px solid grey; border-radius: 5px;text-align: center }"
            "QProgressBar::chunk {background-color: red}"
        )

    def init_display_char(self):
        self.char = QLabel(self.centralwidget)
        self.char.setGeometry(QRect(350, 180, 600, 600))
        query = self.myDataBase.get(f"SELECT path_char FROM player WHERE id={constinfo.player_id}")
        self.char.setPixmap(QPixmap(query[0]))

        self.char.setScaledContents(True)

    def init_lineedit(self):
        self.room = QLineEdit(self)
        self.room.setPlaceholderText("Please Enter The Room Number")
        self.room.setGeometry(880, 210, 260, 30)
        self.room.setStyleSheet(constinfo.stylesheet_lineedit)
        self.room.setAlignment(Qt.AlignCenter)
        self.room.setMaxLength(6)

    def init_subject(self):

        subject = self.myDataBase.get("SELECT DISTINCT id,subject FROM quiz")

        self.scroll_subject_choose = QComboBox(self)
        self.scroll_subject_choose.setGeometry(950, 300, 100, 30)
        self.scroll_subject_choose.setStyleSheet(
            "QComboBox {  border-radius: 3px; }" "QComboBox QAbstractItemView {  border-radius: 3px; }"
        )
        if subject is None:
            self.scroll_subject_choose.addItem("Aucun quiz")
            return False
        for sub in subject:
            self.scroll_subject_choose.addItem(sub.pop())

    def init_button(self):
        self.btn_join_room = QPushButton("Rejoindre", self)
        self.btn_join_room.resize(150, 60)
        self.btn_join_room.move(565, 780)
        self.btn_join_room.clicked.connect(self.join_room)
        self.btn_join_room.setStyleSheet(constinfo.stylesheet_main_button)

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
