from PyQt5.QtWidgets import QLabel, QWidget
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPixmap
from database import Database
import ui
import constinfo
import uimainmenu
from statistics import mean


class WindowStat(ui.Window):
    def __init__(self):
        ui.Window.__init__(self, "Akagame | Connection")
        self.init_window()
        self.init_background("img/imgbckg.jpg")
        self.init_title("Statistiques")

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.centralwidget = QWidget(self)

        self.init_display_char()
        self.init_display_gold()

        self.setCentralWidget(self.centralwidget)

        subject = self.myDataBase.get(f"SELECT subject,mark FROM marks WHERE account_id={constinfo.account_id}")
        self.french_marks = []
        self.english_marks = []
        self.maths_marks = []
        self.history_marks = []

        for sub in subject:
            sub_pooped = sub[0].pop()
            if sub_pooped == "FRENCH":
                self.french_marks.append(sub[1])
            elif sub_pooped == "ENGLISH":
                self.english_marks.append(sub[1])
            elif sub_pooped == "MATHS":
                self.maths_marks.append(sub[1])
            elif sub_pooped == "HISTORY":
                self.history_marks.append(sub[1])

        self.init_lineedit()

        self.btn_return = ui.ReturnButton(uimainmenu.WindowMainMenu, self.close, parent=self.centralwidget)
        self.btn_return.resize(150, 60)
        self.btn_return.move(565, 750)
        self.btn_return.setStyleSheet(
            "QPushButton { font-size: 20px; border : 2px solid white; border-radius : 20px }"
            "QPushButton:hover { background-color: rgba(50, 50, 50, 0.5); font-size: 20px; border : 2px solid white; border-radius : 20px }"
            "QPushButton:pressed { background-color: rgba(250, 250, 250, 0.5); font-size: 20px; border : 2px solid white; border-radius : 20px }"
        )

        self.show()

    def note_color(self, subject_marks, subject_note):
        moy = mean(subject_marks)
        if moy > 15:
            subject_note.setStyleSheet("font-size : 27px; color : green")
        elif moy > 10:
            subject_note.setStyleSheet("font-size : 27px; color : yellow")
        else:
            subject_note.setStyleSheet("font-size : 27px; color : red")

    def init_display_char(self):
        self.char = QLabel(self.centralwidget)
        self.char.setGeometry(QRect(385, 230, 500, 500))
        query = self.myDataBase.get(f"SELECT path_char FROM player WHERE id={constinfo.player_id}")
        self.char.setPixmap(QPixmap(query[0]))
        self.char.setScaledContents(True)

    def init_display_gold(self):
        self.gold = QLabel(self.centralwidget)
        self.gold.setGeometry(QRect(100, 20, 120, 120))
        self.gold.setPixmap(QPixmap("img/gold.png"))
        self.gold.setScaledContents(True)

        self.gold_num = QLabel(self)
        self.gold_num.setGeometry(255, 60, 250, 50)
        print(self.myDataBase.get(f"SELECT gold FROM player WHERE id={constinfo.player_id}")[0])
        self.gold_num.setText(str(self.myDataBase.get(f"SELECT gold FROM player WHERE id={constinfo.player_id}")[0]))
        self.gold_num.setStyleSheet("font-size : 30px;")

    def init_display_xp(self):
        self.char = QLabel(self.centralwidget)
        self.char.setGeometry(QRect(385, 230, 500, 500))
        query = self.myDataBase.get(f"SELECT path_char FROM player WHERE id={constinfo.player_id}")
        self.char.setPixmap(QPixmap(query[0]))

        self.char.setScaledContents(True)

    def init_lineedit(self):
        self.french = QLabel(self)
        self.french.setGeometry(960, 45, 300, 60)
        self.french.setText("Français")
        self.french.setStyleSheet("font-size : 27px;")

        self.english = QLabel(self)
        self.english.setGeometry(960, 100, 300, 60)
        self.english.setText("Anglais")
        self.english.setStyleSheet("font-size : 27px;")

        self.maths = QLabel(self)
        self.maths.setGeometry(960, 155, 300, 60)
        self.maths.setText("Maths")
        self.maths.setStyleSheet("font-size : 27px;")

        self.history = QLabel(self)
        self.history.setGeometry(960, 210, 300, 60)
        self.history.setText("Histoire")
        self.history.setStyleSheet("font-size : 27px;")

        self.french_note = QLabel(self)
        self.french_note.setGeometry(1100, 45, 600, 60)
        if self.french_marks != []:
            self.french_note.setText(str(mean(self.french_marks)))
            self.note_color(self.french_marks, self.french_note)
        else:
            self.french_note.setText("Pas de note")
            self.french_note.setStyleSheet("font-size : 27px;")

        self.english_note = QLabel(self)
        self.english_note.setGeometry(1100, 100, 600, 60)
        if self.english_marks != []:
            self.english_note.setText(str(mean(self.english_marks)))
            self.note_color(self.english_marks, self.english_note)
        else:
            self.english_note.setText("Pas de note")
            self.english_note.setStyleSheet("font-size : 27px;")

        self.maths_note = QLabel(self)
        self.maths_note.setGeometry(1100, 155, 600, 60)
        if self.maths_marks != []:
            self.maths_note.setText(str(mean(self.maths_marks)))
            self.note_color(self.maths_marks, self.maths_note)
        else:
            self.maths_note.setText("Pas de note")
            self.maths_note.setStyleSheet("font-size : 27px;")

        self.history_note = QLabel(self)
        self.history_note.setGeometry(1100, 210, 600, 60)
        if self.history_marks != []:
            self.history_note.setText(str(mean(self.history_marks)))
            self.note_color(self.history_marks, self.history_note)
        else:
            self.history_note.setText("Pas de note")
            self.history_note.setStyleSheet("font-size : 27px;")

