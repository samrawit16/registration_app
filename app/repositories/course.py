from database import get_db_connection


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