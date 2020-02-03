from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QMessageBox
import sys
from database import Database

SQL_INSERT = 'INSERT INTO {table}({columns}) VALUES ({placeholders})'


class WindowConnect(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Insert data"
        self.top = 50
        self.left = 100
        self.width = 1000
        self.height = 800

        self.initWindow()

    def initWindow(self):

        self.lineedit1 = QLineEdit(self)
        self.lineedit1.setPlaceholderText("Please Enter Your name")
        self.lineedit1.setGeometry(200, 100, 200, 30)

        self.lineedit2 = QLineEdit(self)
        self.lineedit2.setPlaceholderText("Please Enter Your password")
        self.lineedit2.setGeometry(200, 150, 200, 30)

        self.lineedit3 = QLineEdit(self)
        self.lineedit3.setPlaceholderText("Please Enter Your Emai")
        self.lineedit3.setGeometry(200, 200, 200, 30)

        self.button = QPushButton("Insert Data", self)
        self.button.setGeometry(200, 250, 100, 30)
        self.button.clicked.connect(self.insertData)

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()

    def insertData(self):
        mysql_config = {"host": "localhost", "user": "root",
                        "passwd": "", "database": "akagame"}

        myDataBase = Database(mysql_config)
        myDataBase.connect()
        columns = ('login', 'password', 'email')

        table = 'account'
        query = SQL_INSERT.format(
            columns=','.join(columns), table=table,
            placeholders=','.join(['%s' for i in range(len(columns))])
        )
        myDataBase.post(query, (self.lineedit1.text(),
                                self.lineedit2.text(), self.lineedit3.text()))

        QMessageBox.about(self, "Connection", "Data inserted Successfully")
        self.close()
