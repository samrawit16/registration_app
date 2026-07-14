from pydantic import BaseModel
class Student(BaseModel):
    name: str
    age: int
    country: str
    email: str
    id_number: int