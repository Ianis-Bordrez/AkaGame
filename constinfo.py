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

account_id = None
account_status = None
player_id = None
