from database import Database
import sys
from PyQt5.QtWidgets import QApplication

from ui import Window
from uiinsertDB import WindowConnect


if __name__ == '__main__':
    # mysql_config = {"host": "localhost", "user": "root",
    #                 "passwd": "", "database": "akagame"}

    # myDataBase = Database(mysql_config)
    # myDataBase.connect()

    # res = myDataBase.get("SELECT * FROM account")

    # columns = ('login', 'password', 'email')
    # table = 'account'

    # query = SQL_INSERT.format(
    #     columns=','.join(columns), table=table,
    #     placeholders=','.join(['%s' for i in range(len(columns))])

    # )
    # myDataBase.post(query, ('Laulau', 'ezff', 'lau@gmail.com'))

    App = QApplication(sys.argv)
    Window = Window()
    Window2 = WindowConnect()
    sys.exit(App.exec())
