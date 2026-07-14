from fastapi import APIRouter, HTTPException, status
from schema.teacher import Teacher
from repositories.teacher import (
    add_teacher,
    get_teachers,
    update_teacher,
    delete_teacher
)

router = APIRouter(prefix="/teachers", tags=["teachers"])

@router.get("")
def list_teachers():
    raw_teachers = get_teachers()
    return [dict(row) for row in raw_teachers]

@router.post("", status_code=status.HTTP_201_CREATED)
def register_teacher(teacher: Teacher):
    add_teacher(
        teacher.name, 
        teacher.email, 
        teacher.department, 
        teacher.office_number, 
        teacher.employee_id
    )
    return {"message": "Teacher registered successfully", "teacher": teacher}

@router.put("/{teacher_id}")
def edit_teacher(teacher_id: int, teacher: Teacher):
    updated = update_teacher(
        teacher_id, 
        teacher.name, 
        teacher.email, 
        teacher.department, 
        teacher.office_number, 
        teacher.employee_id
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return {"message": "Teacher updated successfully"}

@router.delete("/{teacher_id}")
def remove_teacher(teacher_id: int):
    deleted = delete_teacher(teacher_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return {"message": "Teacher deleted successfully"}
