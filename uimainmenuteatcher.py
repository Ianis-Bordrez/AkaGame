from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton
from database import Database
import constinfo
import ui


class WindowTeatcher(ui.Window):
    def __init__(self):
        ui.Window.__init__(self, "AkaGame | Teatcher main window")
        self.init_window()
        self.init_background("img/bckg_create_char.jpg")
        self.show()
