from PyQt5.QtWidgets import QLabel, QWidget
from PyQt5.QtCore import Qt
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

        self.centralwidget = QWidget(self)
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

        self.show()

    def init_lineedit(self):
        self.french = QLabel(self)
        self.french.setGeometry(350, 270, 300, 60)
        self.french.setText("Français")
        self.french.setStyleSheet("font-size : 27px;")

        self.english = QLabel(self)
        self.english.setGeometry(350, 360, 300, 60)
        self.english.setText("Anglais")
        self.english.setStyleSheet("font-size : 27px;")

        self.maths = QLabel(self)
        self.maths.setGeometry(350, 450, 300, 60)
        self.maths.setText("Maths")
        self.maths.setStyleSheet("font-size : 27px;")

        self.history = QLabel(self)
        self.history.setGeometry(350, 540, 300, 60)
        self.history.setText("Histoire")
        self.history.setStyleSheet("font-size : 27px;")

        self.french_note = QLabel(self)
        self.french_note.setGeometry(650, 270, 600, 60)
        if self.french_marks != []:
            self.french_note.setText(str(mean(self.french_marks)))
        else:
            self.french_note.setText("Pas de note")
        self.french_note.setStyleSheet("font-size : 27px;")

        self.english_note = QLabel(self)
        self.english_note.setGeometry(650, 360, 600, 60)
        if self.english_marks != []:
            self.english_note.setText(str(mean(self.english_marks)))
        else:
            self.english_note.setText("Pas de note")
        self.english_note.setStyleSheet("font-size : 27px;")

        self.maths_note = QLabel(self)
        self.maths_note.setGeometry(650, 450, 600, 60)
        print(self.maths_marks)
        if self.maths_marks != []:
            self.maths_note.setText(str(mean(self.maths_marks)))
        else:
            self.maths_note.setText("Pas de note")
        self.maths_note.setStyleSheet("font-size : 27px;")

        self.history_note = QLabel(self)
        self.history_note.setGeometry(650, 540, 600, 60)
        if self.history_marks != []:
            self.history_note.setText(str(mean(self.history_marks)))
        else:
            self.history_note.setText("Pas de note")
        self.history_note.setStyleSheet("font-size : 27px;")
