import datetime

from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    description: str | None = None
    author: str
    price: int
    published_year: int


class Employee(BaseModel):
    id: int
    first_name: str
    last_name: str
    date_joined: datetime.date
    age: int
    city: str
    library_id: int
    is_active: bool
    salary: int
