from sqlalchemy import Column, Integer, String, ForeignKey, TEXT, DATE,BOOLEAN
from sqlalchemy.orm import relationship
from app.database import Base


class Author(Base):
	__tablename__ = 'authors'
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String)

	books = relationship('Book', back_populates='author')


class Book(Base):
	__tablename__ = 'books'
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String)
	description = Column(TEXT)
	author_id = Column(Integer, ForeignKey('authors.id'))
	price = Column(Integer)
	published_year = Column(Integer)

	author = relationship('Author', back_populates='books')


class Employee(Base):
	__tablename__ = 'employees'
	id = Column(Integer, primary_key=True, index=True)
	first_name = Column(String)
	last_name = Column(String)
	date_joined = Column(DATE)
	age = Column(Integer)
	city = Column(String)
	library_id = Column(Integer)
	is_active = Column(BOOLEAN)
	salary = Column(Integer)


