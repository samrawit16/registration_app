from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional
import database

app = FastAPI(title="Extended School Registration API")


database.create_table()


class Student(BaseModel):
    name: str
    age: int
    country: str
    email: str
    id_number: int

class Teacher(BaseModel):
    name: str
    email: str
    department: str
    office_number: str
    employee_id: int

class Course(BaseModel):
    title: str
    course_code: str
    credits: int
    department: str
    teacher_id: Optional[int] = None


@app.get("/")
def home():
    return {"message": "Welcome to my updated school server"}

#student end points
@app.get("/students")
def list_students():
    raw_students = database.get_students()
    return [dict(row) for row in raw_students]

@app.post("/students", status_code=status.HTTP_201_CREATED)
def register_student(student: Student):
    database.add_student(student.name, student.age, student.email, student.country, student.id_number)
    return {"message": "Student registered successfully", "student": student}

@app.put("/students/{student_id}")
def edit_student(student_id: int, student: Student):
    updated = database.update_student(student_id, student.name, student.age, student.email, student.country, student.id_number)
    if not updated:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student updated successfully"}

@app.delete("/students/{student_id}")
def remove_student(student_id: int):
    deleted = database.delete_student(student_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}

# teachers end point
@app.get("/teachers")
def list_teachers():
    raw_teachers = database.get_teachers()
    return [dict(row) for row in raw_teachers]

@app.post("/teachers", status_code=status.HTTP_201_CREATED)
def register_teacher(teacher: Teacher):
    database.add_teacher(teacher.name, teacher.email, teacher.department, teacher.office_number, teacher.employee_id)
    return {"message": "Teacher registered successfully", "teacher": teacher}

@app.put("/teachers/{teacher_id}")
def edit_teacher(teacher_id: int, teacher: Teacher):
    updated = database.update_teacher(teacher_id, teacher.name, teacher.email, teacher.department, teacher.office_number, teacher.employee_id)
    if not updated:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return {"message": "Teacher updated successfully"}

@app.delete("/teachers/{teacher_id}")
def remove_teacher(teacher_id: int):
    deleted = database.delete_teacher(teacher_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return {"message": "Teacher deleted successfully"}

#courses end points
@app.get("/courses")
def list_courses():
    raw_courses = database.get_courses()
    return [dict(row) for row in raw_courses]

@app.post("/courses", status_code=status.HTTP_201_CREATED)
def register_course(course: Course):
    database.add_course(course.title, course.course_code, course.credits, course.department, course.teacher_id)
    return {"message": "Course registered successfully", "course": course}

@app.put("/courses/{course_id}")
def edit_course(course_id: int, course: Course):
    updated = database.update_course(course_id, course.title, course.course_code, course.credits, course.department, course.teacher_id)
    if not updated:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"message": "Course updated successfully"}

@app.delete("/courses/{course_id}")
def remove_course(course_id: int):
    deleted = database.delete_course(course_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"message": "Course deleted successfully"}
