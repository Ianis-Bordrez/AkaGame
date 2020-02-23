from PyQt5.QtWidgets import QLabel, QWidget
from PyQt5.QtCore import Qt
from database import Database
import ui
import constinfo
import uimainmenu


class WindowStat(ui.Window):
    def __init__(self):
        ui.Window.__init__(self, "Akagame | Connection")
        self.init_window()
        self.init_background("img/imgbckg.jpg")

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.init_lineedit()

        self.btn_return = ui.ReturnButton(uimainmenu.WindowMainMenu, self.close, parent=self.centralwidget)

        self.show()

    def init_lineedit(self):
        self.french = QLabel(self.centralwidget)
        self.french.setGeometry(440, 230, 400, 30)
        self.french.setText("Français")
        self.french.setStyleSheet(
            "background-color : transparent; color : black; border : 1px solid black; border-radius: 5px; font-size : 17px,  text-align : center;"
        )
