from database import Database

SQL_INSERT = 'INSERT INTO {table}({columns}) VALUES ({placeholders})'

if __name__ == '__main__':
    mysql_config = {"host": "localhost", "user": "root",
                    "passwd": "", "database": "akagame"}

    myDataBase = Database(mysql_config)
    myDataBase.connect()

    res = myDataBase.get("SELECT * FROM account")

    columns = ('login', 'password', 'email')
    table = 'account'

    query = SQL_INSERT.format(
        columns=','.join(columns), table=table,
        placeholders=','.join(['%s' for i in range(len(columns))])

    )
    myDataBase.post(query, ('Laulau', 'ezff', 'lau@gmail.com'))
