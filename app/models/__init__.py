from models import student, teacher, course
def create_table():
    student.create_table()
    teacher.create_table()
    course.create_table()