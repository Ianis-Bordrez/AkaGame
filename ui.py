from PyQt5.QtWidgets import QMainWindow, QLabel, QAbstractButton
from PyQt5.QtGui import QPixmap, QPainter


class Window(QMainWindow):
    def __init__(self, title, width=1280, height=900):
        super().__init__()
        self.width = width
        self.height = height
        self.windowTitle = title

    def init_window(self):
        self.setGeometry(300, 50, self.width, self.height)
        self.setWindowTitle(self.windowTitle)

    def init_background(self, path):
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap(path))
        self.background.setGeometry(0, 0, self.width, self.height)


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
