from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QMessageBox
import sys
from database import Database

from uilogin import WindowLogin


if __name__ == '__main__':
    App = QApplication(sys.argv)
    Window = WindowLogin()
    sys.exit(App.exec())
