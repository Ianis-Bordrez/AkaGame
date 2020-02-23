SQL_QUERY = "SELECT {columns} FROM {table} WHERE project_id = {project_id}"
SQL_INSERT = "INSERT INTO {table}({columns}) VALUES ({placeholders})"
SQL_UPDATE = """
    UPDATE {table}
    SET {placeholders}
    WHERE project_id = {project_id}
"""

mysql_config = {
    "host": "mysql-ianis-bordrez.alwaysdata.net",
    "user": "173945_akagame",
    "passwd": "AK4ee65rù51",
    "database": "ianis-bordrez_akagame",
}

columns_create_account = ("login", "password", "email", "status", "subject")
columns_create_player = ("account_id", "name", "path_char", "gender")
columns_create_quiz = ("quiz_id", "subject", "name")
columns_create_question = ("quiz_id", "question", "answer_true", "answer_2", "answer_3", "answer_4")
columns_create_marks = ("account_id", "subject", "quiz_id", "mark")

account_id = None
account_status = None
player_id = None
player_char = ""
teatcher_subject = None

char_img_m = ("char_m_1.png", "char_m_2.png", "char_m_3.png", "char_m_4.png")
char_img_w = ("char_w_1.png", "char_w_2.png", "char_w_3.png", "char_w_4.png")

stylesheet_lineedit = (
    "background-color : transparent; color : black; border : 1px solid black; border-radius: 5px; font-size : 17px;"
)

stylesheet_main_button = """
    QPushButton { background-color: transparent; font-size: 20px; border : 2px solid black; border-radius : 20px; }
    QPushButton:hover { background-color: rgba(50, 50, 50, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px; }
    QPushButton:pressed { background-color: rgba(250, 250, 250, 0.5); font-size: 20px; border : 2px solid black; border-radius : 20px; }
"""

