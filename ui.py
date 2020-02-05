from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QPixmap


class Window(QMainWindow):
    def __init__(self, title, width=1200, height=800):
        super().__init__()
        self.width = width
        self.height = height
        self.windowTitle = title

    def init_window(self):
        self.setGeometry(600, 200, self.width, self.height)
        self.setWindowTitle(self.windowTitle)

    def init_background(self, path):
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap(path))
        self.background.setGeometry(0, 0, self.width, self.height)
