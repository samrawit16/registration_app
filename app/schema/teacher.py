from pydantic import BaseModel

class Teacher(BaseModel):
    name: str
    email: str
    department: str
    office_number: str
    employee_id: int
