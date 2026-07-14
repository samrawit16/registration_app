from pydantic import BaseModel
from typing import Optional

class Course(BaseModel):
    title: str
    course_code: str
    credits: int
    department: str
    teacher_id: Optional[int] = None