from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

from database import Database
import constinfo
import ui


class WindowGame(ui.Window):
    def __init__(self):
        ui.Window.__init__(self, "AkaGame | Game")
        self.init_window()
        self.init_background("img/bckg_create_char.jpg")
        self.init_button()
        self.init_lineedit()
        self.show()

    def init_lineedit(self):
        pass

    def init_button(self):
        pass

