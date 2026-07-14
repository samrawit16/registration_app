from database import get_db_connection
def create_table():
    with get_db_connection() as connection:
        connection.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                course_code TEXT NOT NULL,
                credits INTEGER NOT NULL,
                department TEXT NOT NULL,
                teacher_id INTEGER
            )
        ''')