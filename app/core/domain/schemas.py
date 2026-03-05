from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


class CourseCreate(BaseModel):
    title: str
    description: str
    workload: int


class EnrollmentCreate(BaseModel):
    user_id: int
    course_id: int