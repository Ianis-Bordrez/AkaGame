from PyQt5.QtWidgets import (QApplication, QLabel, QWidget)


class MouseTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(90, 50, 1280, 900)
        self.setWindowTitle('Mouse Tracker')
        self.label = QLabel(self)
        self.label.resize(200, 40)
        self.show()

    def mouseMoveEvent(self, event):
        self.label.setText('Mouse coords: ( %d : %d )' %
                           (event.x(), event.y()))
