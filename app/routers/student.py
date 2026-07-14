from fastapi import APIRouter, HTTPException
from schema.student import Student
from repositories.student import (
    add_student,
    get_students,
    update_student,
    delete_student
)

router = APIRouter(prefix="/students", tags=["students"])

@router.post("")
def register_student(student: Student):
    add_student(student.name, student.age, student.email, student.country, student.id_number)
    return {"message": "Student registered successfully", "student": student}

@router.get("")
def list_students():
    raw_students = get_students()
    return [dict(row) for row in raw_students]

@router.put("/{student_id}")
def edit_student(student_id: int, student: Student):
    updated = update_student(student_id, student.name, student.age, student.email, student.country, student.id_number)
    if not updated:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student updated successfully"}

@router.delete("/{student_id}")
def remove_student(student_id: int):
    deleted = delete_student(student_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}
