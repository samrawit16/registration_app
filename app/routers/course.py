from fastapi import APIRouter, HTTPException, status
from schema.course import Course
from repositories.course import (
    add_course,
    get_courses,
    update_course,
    delete_course
)

router = APIRouter(prefix="/courses", tags=["courses"])

@router.get("")
def list_courses():
    raw_courses = get_courses()
    return [dict(row) for row in raw_courses]

@router.post("", status_code=status.HTTP_201_CREATED)
def register_course(course: Course):
    add_course(
        course.title, 
        course.course_code, 
        course.credits, 
        course.department, 
        course.teacher_id
    )
    return {"message": "Course registered successfully", "course": course}

@router.put("/{course_id}")
def edit_course(course_id: int, course: Course):
    updated = update_course(
        course_id, 
        course.title, 
        course.course_code, 
        course.credits, 
        course.department, 
        course.teacher_id
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"message": "Course updated successfully"}

@router.delete("/{course_id}")
def remove_course(course_id: int):
    deleted = delete_course(course_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"message": "Course deleted successfully"}
