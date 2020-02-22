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
columns_create_player = ("account_id", "name", "class")
columns_create_quiz = ("quiz_id", "subject", "name")
columns_create_question = ("quiz_id", "question", "answer_true", "answer_2", "answer_3", "answer_4")
columns_create_marks = ("account_id", "subject", "quiz_id", "mark")

account_id = None
account_status = None
player_id = None
teatcher_subject = None
