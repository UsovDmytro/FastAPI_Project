from sqlalchemy.orm import Session
from app.models import Book, Employee, Author
from fastapi import HTTPException
from app.schemas import AuthorCreate, EmployeeCreate, BookCreate


def book_list(db: Session):
	return db.query(Book).all()


def employee_list(db: Session, query_params):
	return db.query(Employee).filter((query_params.first_name is None or Employee.first_name == query_params.first_name) and
												 (query_params.age is None or Employee.age == query_params.age) and
												 (query_params.city is None or Employee.city == query_params.city))


def author_list(db: Session):
	return db.query(Author).all()


def book_retrieve(db: Session, book_id: int):
	book = db.query(Book).filter(Book.id == book_id).first()
	if book is None:
		raise HTTPException(status_code=404, detail="Книги с таким id не существует")

	return book


def author_retrieve(db: Session, author_id: int):
	author = db.query(Author).filter(Author.id == author_id).first()
	if author is None:
		raise HTTPException(status_code=404, detail="Автора с таким id не существует")

	return author


def employee_retrieve(db: Session, employee_id: int):
	employee = db.query(Employee).filter(Employee.id == employee_id).first()
	if employee is None:
		raise HTTPException(status_code=404, detail="Сотрудника с таким id не существует")

	return employee


def author_create(db: Session, author: AuthorCreate):
	author_model = Author(**author.model_dump())
	db.add(author_model)
	db.commit()
	db.refresh(author_model)
	return author_model


def employee_create(db: Session, employee: EmployeeCreate):
	employee_model = Employee(**employee.model_dump())
	db.add(employee_model)
	db.commit()
	db.refresh(employee_model)
	return employee_model


def book_create(db: Session, book: BookCreate):
	book_model = Book(**book.model_dump())
	db.add(book_model)
	db.commit()
	db.refresh(book_model)
	return book_model


def book_delete(db: Session, book_id: int):
	book = db.query(Book).filter(Book.id == book_id).first()
	if book is None:
		raise HTTPException(status_code=404, detail="Книги с таким id не существует")
	db.delete(book)
	db.commit()


def author_delete(db: Session, author_id: int):
	author = db.query(Author).filter(Author.id == author_id).first()
	if author is None:
		raise HTTPException(status_code=404, detail="Автора с таким id не существует")
	db.delete(author)
	db.commit()


def employee_delete(db: Session, employee_id: int):
	employee = db.query(Employee).filter(Employee.id == employee_id).first()
	if employee is None:
		raise HTTPException(status_code=404, detail="Сотрудника с таким id не существует")
	db.delete(employee)
	db.commit()


def author_update(db: Session, author_id: int, author: AuthorCreate):
	author_db = db.query(Author).filter(Author.id == author_id).first()
	if author_db is None:
		raise HTTPException(status_code=404, detail="Автора с таким id не существует")
	for key, value in author.model_dump().items():
		setattr(author_db, key, value)
	db.commit()
	return author_db


def employee_update(db: Session, employee_id: int, employee: EmployeeCreate):
	employee_db = db.query(Employee).filter(Employee.id == employee_id).first()
	if employee_db is None:
		raise HTTPException(status_code=404, detail="Автора с таким id не существует")
	for key, value in employee.model_dump().items():
		setattr(employee_db, key, value)
	db.commit()
	return employee_db


def book_update(db: Session, book_id: int, book: BookCreate):
	book_db = db.query(Book).filter(Book.id == book_id).first()
	if book_db is None:
		raise HTTPException(status_code=404, detail="Автора с таким id не существует")
	for key, value in book.model_dump().items():
		setattr(book_db, key, value)
	db.commit()
	return book_db