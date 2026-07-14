from fastapi import FastAPI
from routers import student, teacher, course

app = FastAPI()

app.include_router(student.router)
app.include_router(teacher.router)
app.include_router(course.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Registration System API. Go to /docs for documentation."}
