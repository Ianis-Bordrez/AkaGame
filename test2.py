from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QMessageBox, QLabel, QComboBox, QWidget
from PyQt5.QtCore import Qt
from database import Database
import uilogin
import constinfo
import ui


class WindowCreateAccount(ui.Window):
    def __init__(self):
        ui.Window.__init__(self, "Akagame | Create account")
        self.init_window()
        self.init_background("img/imgbckg.jpg")
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.btn_return = ui.ReturnButton(uilogin.WindowLogin, self.close, parent=self.centralwidget)

        self.test = -1

        self.show()


from PyQt5.QtWidgets import QApplication
import sys
from uilogin import WindowLogin


if __name__ == "__main__":
    App = QApplication(sys.argv)
    Window = WindowCreateAccount()
    sys.exit(App.exec())
