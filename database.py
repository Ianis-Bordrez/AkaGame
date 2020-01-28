import mysql.connector as mysql


class DatabaseError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Database:
    def __init__(self, host, user, database, passwd=""):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database
        self.mydb = self.connect()
        self.cursor = self.mydb.cursor()

    def connect(self):
        try:
            conn = mysql.connect(
                host=self.host, user=self.user, passwd=self.passwd, database=self.database)
            if conn.is_connected():
                return conn
        except mysql.Error as err:
            raise DatabaseError(err)

    def mysql_query_get(self, query):
        try:
            rows = None
            self.cursor.execute(query)
            _rows = self.cursor.fetchall()
            if _rows:
                rows = list()
                for row in _rows:
                    rows.append(row)
                if len(rows) == 1:
                    rows = rows[0]
            return rows
        except mysql.Error as e:
            msg = "Failure in executing query {0}. Error: {1}".format(query, e)
            raise DatabaseError(msg)


myDataBase = Database("localhost", "root", "akagame", passwd="t")

res = myDataBase.mysql_query_get("SELECT * FROM account")

for row in res:
    print(row)

# print(mydb)

# if mydb:
#     print("Connection successful !")
# else:
#     print("Connection unsuccessful !")

# mycursor = mydb.cursor()

# mycursor.execute("Show tables")

# for db in mycursor:
#     print(db)

# sqlInsert = "INSERT INTO account(login,password,email) VALUES(%s,%s,%s)"

# users = ("Laurent", "uyzyad", "laurent@gmail.com")

# # mycursor.execute(sqlInsert, users)
# # mydb.commit()

# mycursor.execute("SELECT * FROM account")
# myresult = mycursor.fetchone()
# myresult2 = mycursor.fetchall()

# for row in myresult:
#     print(row)

# print("---"*7)

# for row in myresult2:
#     print(row)
