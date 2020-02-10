from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QMainWindow):
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



class Ui_MainWindow(Window):
    def __init__(self):
        Window.__init__(self, "TEST")
        self.setupUi()

    def setupUi(self):
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 841, 511))
        self.photo.setPixmap(QtGui.QPixmap("img/char/char_m_1.png"))
        self.photo.setScaledContents(True)
        self.cat = QtWidgets.QPushButton(self.centralwidget)
        self.cat.setGeometry(QtCore.QRect(0, 510, 411, 41))
        self.dog = QtWidgets.QPushButton(self.centralwidget)
        self.dog.setGeometry(QtCore.QRect(410, 510, 391, 41))
        self.setCentralWidget(self.centralwidget)

        self.dog.clicked.connect(self.show_dog)
        self.cat.clicked.connect(self.show_cat)

        self.show()


    def show_dog(self):
        self.photo.setPixmap(QtGui.QPixmap("img/char/char_m_1.png"))

    def show_cat(self):
        self.photo.setPixmap(QtGui.QPixmap("img/char/char_m_2.png"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    sys.exit(app.exec_())