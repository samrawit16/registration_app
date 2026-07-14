from database import get_db_connection
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
