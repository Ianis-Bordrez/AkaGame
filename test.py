from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys


class MyMainWindow(QMainWindow):
    def __init__(self, title, width=1280, height=900):
        super().__init__()
        self.width = width
        self.height = height
        self.windowTitle = title
        self.button = QPushButton("Button", self)
        self.button.clicked.connect(self.showButton)
        self.test = 0

    def init_window(self):
        self.setGeometry(300, 50, self.width, self.height)
        self.setWindowTitle(self.windowTitle)

    def init_background(self, path):
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap(path))
        self.background.setGeometry(0, 0, self.width, self.height)

    def showButton(self):
        if self.test == 0:
            self.form_widget = FormWidget()
            self.setCentralWidget(self.form_widget)
        else:
            self.form_widget.hide()


class FormWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        self.button1 = QPushButton("Button 1")
        self.layout.addWidget(self.button1)

        self.button2 = QPushButton("Button 2")
        self.layout.addWidget(self.button2)

        self.setLayout(self.layout)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    foo = MyMainWindow("test")
    foo.show()
    sys.exit(App.exec())
