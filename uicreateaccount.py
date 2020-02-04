from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QMessageBox
import sys
from database import Database
import uilogin

SQL_INSERT = 'INSERT INTO {table}({columns}) VALUES ({placeholders})'


class WindowCreateAccount(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title="Alkutiedot"
        self.top=600
        self.left=200
        self.width=500
        self.height=500

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

        self.button = QPushButton("Create", self)
        self.button.setGeometry(200, 250, 100, 30)
        self.button.clicked.connect(self.insertData)

        self.button=QPushButton("Return", self)
        self.button.move(100,400)
        self.button.clicked.connect(self.btn_return)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
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

        QMessageBox.about(self, "Connection", "Account created Successfully")

        self.close()
        self.next=uilogin.WindowLogin()

    def quit(self):
        print('close clicked')
        self.close()

    def btn_return(self):
        self.close()
        self.next=uilogin.WindowLogin()
