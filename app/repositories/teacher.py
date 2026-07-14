from database import get_db_connection

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

