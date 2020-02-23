from PyQt5.QtWidgets import QApplication
import sys
from uilogin import WindowLogin


if __name__ == "__main__":
    App = QApplication(sys.argv)
    Window = WindowLogin()
    sys.exit(App.exec())
eleve2

