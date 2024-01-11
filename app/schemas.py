import datetime
from pydantic import BaseModel


class AuthorBase(BaseModel):
    name: str


class BookBase(BaseModel):
    name: str
    description: str | None = None
    author_id: int
    price: int
    published_year: int


class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    date_joined: datetime.date
    age: int
    city: str
    library_id: int
    is_active: bool
    salary: int


class EmployeeCreate(EmployeeBase):
    pass


class BookCreate(BookBase):
    pass


class AuthorCreate(AuthorBase):
    pass


class AuthorSchema(AuthorBase):
    id: int

    class Config:
        orm_mode = True


class BookSchema(BookBase):
    id: int

    class Config:
        orm_mode = True


class EmployeeSchema(EmployeeBase):
    id: int

    class Config:
        orm_mode = True


