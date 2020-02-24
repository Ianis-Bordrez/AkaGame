from PyQt5.QtWidgets import QMainWindow, QLabel, QAbstractButton, QPushButton, QWidget
from PyQt5.QtGui import QPixmap, QPainter
from database import Database
from PyQt5.QtCore import QRect, Qt
import constinfo


class Window(QMainWindow):
    def __init__(self, window_title, width=1280, height=900):
        super().__init__()
        self.width = width
        self.height = height
        self.windowTitle = window_title

        self.myDataBase = Database(constinfo.mysql_config)
        self.myDataBase.connect()

    def init_window(self):
        self.setFixedSize(1280, 900)
        self.setWindowTitle(self.windowTitle)

    def init_background(self, path):
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap(path))
        self.background.setGeometry(0, 0, 1280, 900)

    def init_title(self, title):
        self.title = QLabel(self)
        self.title.setText(title)
        self.title.setGeometry(440, 100, 400, 50)
        self.title.setStyleSheet("background-color : transparent; color : black; font-size : 30px;")
        self.title.setAlignment(Qt.AlignCenter)


class PicButton(QAbstractButton):
    def __init__(self, pixmap, pixmap_hover, pixmap_pressed, parent=None):
        super(PicButton, self).__init__(parent)
        self.pixmap = pixmap
        self.pixmap_hover = pixmap_hover
        self.pixmap_pressed = pixmap_pressed

        self.pressed.connect(self.update)
        self.released.connect(self.update)

    def paintEvent(self, event):
        pix = self.pixmap_hover if self.underMouse() else self.pixmap
        if self.isDown():
            pix = self.pixmap_pressed

        painter = QPainter(self)
        painter.drawPixmap(event.rect(), pix)

    def enterEvent(self, event):
        self.update()

    def leaveEvent(self, event):
        self.update()

    def sizeHint(self):
        return self.pixmap.size()


class ReturnButton(QPushButton):
    def __init__(self, previous_window, close_parent_window, name="Retour", x=1100, y=820, parent=None):
        super(ReturnButton, self).__init__(parent)
        self.resize(150, 60)
        self.setText(name)
        self.move(x, y)
        self.clicked.connect(lambda: self.return_login(previous_window, close_parent_window))
        self.setStyleSheet(constinfo.stylesheet_main_button)

    def return_login(self, previous_window, close_parent_window):
        close_parent_window()
        self.next = previous_window()
