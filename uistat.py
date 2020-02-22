from PyQt5.QtWidgets import QApplication, QLineEdit, QPushButton, QMessageBox, QLabel
from PyQt5.QtCore import Qt
from database import Database
import ui
import constinfo
import uicreateaccount
import uimainmenu
import uicreateplayer
import uimainmenuteatcher


class WindowStat(ui.Window):
    def __init__(self):
        ui.Window.__init__(self, "Akagame | Connection")
        self.init_window()
        self.init_background("img/imgbckg.jpg")
        self.init_lineedit()

        self.show()

    def init_lineedit(self):
        self.french = QLabel(self)
        self.french.setGeometry(440, 230, 400, 30)
        self.french.setText(f"Français")
        self.french.setStyleSheet(
            "background-color : transparent; color : black; border : 1px solid black; border-radius: 5px; font-size : 17px,  text-align : center"
        )

