SQL_QUERY = 'SELECT {columns} FROM {table} WHERE project_id = {project_id}'
SQL_INSERT = 'INSERT INTO {table}({columns}) VALUES ({placeholders})'
SQL_UPDATE = '''
    UPDATE {table}
    SET {placeholders}
    WHERE project_id = {project_id}
'''

mysql_config = {"host": "localhost", "user": "root",
                        "passwd": "", "database": "akagame"}

columns_create_account = ('login', 'password', 'email', 'status')
columns_create_player = ('account_id', 'name', 'class')
columns_create_quiz = ('quiz_id', 'subject', 'name')
columns_create_question = ('quiz_id', 'question',
                           'answer_true', 'answer_2', 'answer_3', 'answer_4')

account_id = None
player_id = None
teatcher_subject = None
