import sqlite3
from contextlib import contextmanager

sqlite_file_name = "school.db"

@contextmanager
def get_db_connection():
    conn = sqlite3.connect(sqlite_file_name)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()

def create_table():
    with get_db_connection() as connection:
       
        connection.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                email TEXT NOT NULL,
                country TEXT NOT NULL,
                id_number INTEGER NOT NULL
            )
        ''')
      
        connection.execute('''
            CREATE TABLE IF NOT EXISTS teachers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                department TEXT NOT NULL,
                office_number TEXT NOT NULL,
                employee_id INTEGER NOT NULL
            )
        ''')
      
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


def add_student(name, age, email, country, id_number):
    with get_db_connection() as connection:
        connection.execute(
            'INSERT INTO students (name, age, email, country, id_number) VALUES (?, ?, ?, ?, ?)',
            (name, age, email, country, id_number)
        )

def get_students():
    with get_db_connection() as connection:
        return connection.execute('SELECT * FROM students').fetchall()

def update_student(student_id, name, age, email, country, id_number):
    with get_db_connection() as connection:
        cursor = connection.execute(
            'UPDATE students SET name=?, age=?, email=?, country=?, id_number=? WHERE id=?',
            (name, age, email, country, id_number, student_id)
        )
        return cursor.rowcount > 0

def delete_student(student_id):
    with get_db_connection() as connection:
        cursor = connection.execute('DELETE FROM students WHERE id=?', (student_id,))
        return cursor.rowcount > 0


def add_teacher(name, email, department, office_number, employee_id):
    with get_db_connection() as connection:
        connection.execute(
            'INSERT INTO teachers (name, email, department, office_number, employee_id) VALUES (?, ?, ?, ?, ?)',
            (name, email, department, office_number, employee_id)
        )

def get_teachers():
    with get_db_connection() as connection:
        return connection.execute('SELECT * FROM teachers').fetchall()

def update_teacher(teacher_id, name, email, department, office_number, employee_id):
    with get_db_connection() as connection:
        cursor = connection.execute(
            'UPDATE teachers SET name=?, email=?, department=?, office_number=?, employee_id=? WHERE id=?',
            (name, email, department, office_number, employee_id, teacher_id)
        )
        return cursor.rowcount > 0

def delete_teacher(teacher_id):
    with get_db_connection() as connection:
        cursor = connection.execute('DELETE FROM teachers WHERE id=?', (teacher_id,))
        return cursor.rowcount > 0


def add_course(title, course_code, credits, department, teacher_id):
    with get_db_connection() as connection:
        connection.execute(
            'INSERT INTO courses (title, course_code, credits, department, teacher_id) VALUES (?, ?, ?, ?, ?)',
            (title, course_code, credits, department, teacher_id)
        )

def get_courses():
    with get_db_connection() as connection:
        return connection.execute('SELECT * FROM courses').fetchall()

def update_course(course_id, title, course_code, credits, department, teacher_id):
    with get_db_connection() as connection:
        cursor = connection.execute(
            'UPDATE courses SET title=?, course_code=?, credits=?, department=?, teacher_id=? WHERE id=?',
            (title, course_code, credits, department, teacher_id, course_id)
        )
        return cursor.rowcount > 0

def delete_course(course_id):
    with get_db_connection() as connection:
        cursor = connection.execute('DELETE FROM courses WHERE id=?', (course_id,))
        return cursor.rowcount > 0
