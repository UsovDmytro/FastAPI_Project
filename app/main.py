from typing import List
from fastapi import FastAPI, Query, Depends
from starlette import status
from sqlalchemy.orm import Session
from typing_extensions import Annotated

from app.database import SessionLocal
from app.models import Book, Author, Employee
from app.schemas import BookCreate, AuthorCreate, EmployeeCreate, AuthorSchema, EmployeeSchema, BookSchema
from app import crud

app = FastAPI()


def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()


class GetQueryParam:
	def __init__(self, first_name: Annotated[str | None, Query(min_length=1, max_length=100)] = None,
							age: Annotated[int | None, Query(qe=0)] = None,
							city: Annotated[str | None, Query(min_length=1, max_length=100)] = None):
		self.first_name = first_name
		self.age = age
		self.city = city


@app.get("/books/", status_code=status.HTTP_200_OK)
async def get_book_list(db: Session = Depends(get_db)) -> List[BookCreate]:
	books = crud.book_list(db)
	return books


@app.get("/employees/", status_code=status.HTTP_200_OK)
async def get_employee_list(db: Annotated[Session, Depends(get_db)], query_params: Annotated[GetQueryParam, Depends()]) -> List[EmployeeSchema]:
	employees = crud.employee_list(db, query_params)
	return employees


@app.get("/authors/", status_code=status.HTTP_200_OK)
async def get_book_list(db: Annotated[Session, Depends(get_db)]) -> List[AuthorSchema]:
	authors = crud.author_list(db)
	return authors


@app.get("/employees/{employee_id}", status_code=status.HTTP_200_OK)
async def get_employee(db: Annotated[Session, Depends(get_db)], employee_id: int) -> EmployeeSchema:
	employee = crud.employee_retrieve(db, employee_id)
	return employee


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def get_book(db: Annotated[Session, Depends(get_db)], book_id: int) -> BookSchema:
	book = crud.book_retrieve(db, book_id)
	return book


@app.get("/authors/{author_id}", status_code=status.HTTP_200_OK)
async def get_author(db: Annotated[Session, Depends(get_db)], author_id: int) -> AuthorSchema:
	author = crud.author_retrieve(db, author_id)
	return author


@app.post("/authors/", response_model=AuthorCreate)
def create_author(db: Annotated[Session, Depends(get_db)], author: AuthorCreate):
	author_created = crud.author_create(db, author)
	return author_created


@app.post("/books/", response_model=AuthorCreate)
def create_author(db: Annotated[Session, Depends(get_db)], book: BookCreate):
	book_created = crud.book_create(db, book)
	return book_created


@app.post("/employees/", response_model=AuthorCreate)
def create_author(db: Annotated[Session, Depends(get_db)], employee: EmployeeCreate):
	employee_created = crud.employee_create(db, employee)
	return employee_created


@app.delete("/employees/{employee_id}")
async def delete_employee(db: Annotated[Session, Depends(get_db)], employee_id: int):
	crud.employee_delete(db, employee_id)
	return {"message": "Employee deleted successfully"}


@app.delete("/books/{book_id}")
async def delete_book(db: Annotated[Session, Depends(get_db)], book_id: int):
	crud.book_delete(db, book_id)
	return {"message": "Book deleted successfully"}


@app.delete("/authors/{author_id}")
async def delete_author(db: Annotated[Session, Depends(get_db)], author_id: int):
	crud.author_delete(db, author_id)
	return {"message": "Author deleted successfully"}


@app.put("/authors/{author_id}", response_model=AuthorCreate)
def update_author(db: Annotated[Session, Depends(get_db)], author_id: int, author: AuthorCreate):
	author_updated = crud.author_update(db, author_id, author)
	return author_updated


@app.put("/books/{book_id}", response_model=BookCreate)
def update_book(db: Annotated[Session, Depends(get_db)], book_id: int, book: BookCreate):
	book_updated = crud.book_update(db, book_id, book)
	return book_updated


@app.put("/employees/{employee_id}", response_model=EmployeeCreate)
def update_employee(db: Annotated[Session, Depends(get_db)], employee_id: int, employee: EmployeeCreate):
	employee_updated = crud.employee_update(db, employee_id, employee)
	return employee_updated

