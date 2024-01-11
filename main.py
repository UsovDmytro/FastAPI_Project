from typing import Any

from fastapi import FastAPI, Query, HTTPException
from starlette import status

from schemas import Book, Employee
from typing_extensions import Annotated
from datetime import date


app = FastAPI()

books_data = [
	{"id": 1,
	 "title": "Book 1",
	 "description": "Description 1",
	 "author": "Author 1",
	 "price": 20,
	 "published_year": 2020},

	{"id": 2,
	 "title": "Book 2",
	 "description": "Description 2",
	 "author": "Author 2",
	 "price": 25,
	 "published_year": 2021},

	{"id": 3,
	 "title": "Book 3",
	 "description": "Description 3",
	 "author": "Author 3",
	 "price": 30,
	 "published_year": 2022},

	{"id": 4,
	 "title": "Book 4",
	 "description": "Description 4",
	 "author": "Author 4",
	 "price": 15,
	 "published_year": 2019},

	{"id": 5,
	 "title": "Book 5",
	 "description": "Description 5",
	 "author": "Author 5",
	 "price": 22,
	 "published_year": 2023},

	{"id": 6,
	 "title": "Book 6",
	 "description": "Description 6",
	 "author": "Author 6",
	 "price": 18,
	 "published_year": 2020},

	{"id": 7,
	 "title": "Book 7",
	 "description": "Description 7",
	 "author": "Author 7",
	 "price": 28,
	 "published_year": 2022},

	{"id": 8,
	 "title": "Book 8",
	 "description": "Description 8",
	 "author": "Author 8",
	 "price": 35,
	 "published_year": 2021},

	{"id": 9,
	 "title": "Book 9",
	 "description": "Description 9",
	 "author": "Author 9",
	 "price": 20,
	 "published_year": 2018},

	{"id": 10,
	 "title": "Book 10",
	 "description": "Description 10",
	 "author": "Author 10",
	 "price": 30,
	 "published_year": 2023}
]

employees = [
	{"id": 1,
	 "first_name": "John",
	 "last_name": "Doe",
	 "date_joined": date(2020, 5, 15),
	 "age": 28,
	 "city": "New York",
	 "library_id": 1,
	 "is_active": True,
	 "salary": 50000
	 },
	{"id": 2,
	 "first_name": "Jane",
	 "last_name": "Smith",
	 "date_joined": date(2019, 8, 23),
	 "age": 35,
	 "city": "Los Angeles",
	 "library_id": 1,
	 "is_active": False,
	 "salary": 60000
	 },
	{"id": 3,
	 "first_name": "Bob",
	 "last_name": "Johnson",
	 "date_joined": date(2021, 3, 10),
	 "age": 32, "city": "Chicago",
	 "library_id": 2,
	 "is_active": True,
	 "salary": 55000
	 },
	{"id": 4,
	 "first_name": "Alice",
	 "last_name": "Williams",
	 "date_joined": date(2018, 12, 5),
	 "age": 40,
	 "city": "Houston",
	 "library_id": 2,
	 "is_active": False,
	 "salary": 70000
	 },
	{"id": 5,
	 "first_name": "Charlie",
	 "last_name": "Brown",
	 "date_joined": date(2022, 7, 18),
	 "age": 25,
	 "city": "San Francisco",
	 "library_id": 3,
	 "is_active": True,
	 "salary": 48000
	 },
	{"id": 6,
	 "first_name": "Eva",
	 "last_name": "Davis",
	 "date_joined": date(2020, 1, 30),
	 "age": 29,
	 "city": "Miami",
	 "library_id": 3,
	 "is_active": True,
	 "salary": 52000
	 },
	{"id": 7,
	 "first_name": "David",
	 "last_name": "Miller",
	 "date_joined": date(2017, 6, 8),
	 "age": 45,
	 "city": "Seattle",
	 "library_id": 3,
	 "is_active": False,
	 "salary": 75000
	 },
	{"id": 8,
	 "first_name": "Grace",
	 "last_name": "Jones",
	 "date_joined": date(2019, 11, 12),
	 "age": 31,
	 "city": "Dallas",
	 "library_id": 4,
	 "is_active": True,
	 "salary": 58000
	 },
	{"id": 9,
	 "first_name": "Frank",
	 "last_name": "Taylor",
	 "date_joined": date(2023, 2, 25),
	 "age": 26,
	 "city": "Atlanta",
	 "library_id": 4,
	 "is_active": False,
	 "salary": 63000
	 },
	{"id": 10,
	 "first_name": "Helen",
	 "last_name": "Moore",
	 "date_joined": date(2018, 4, 7),
	 "age": 38,
	 "city": "Boston",
	 "library_id": 5,
	 "is_active": True,
	 "salary": 67000
	 }
]


@app.get("/books/")
async def get_book_list(pricegt: int | None = None, is_active: bool = False):

	if pricegt is not None:
		books = list(filter(lambda x: x['price'] > pricegt, books_data))
		return {"books": books, "is_active": is_active}
	return {"books": books_data, "is_active": is_active}


@app.get("/employees/", status_code=status.HTTP_200_OK)
async def get_employee_list(first_name: Annotated[str | None, Query(min_length=1, max_length=100)] = None,
							age: Annotated[int | None, Query(qe=0)] = None,
							city: Annotated[str | None, Query(min_length=1, max_length=100)] = None):

	if first_name is not None or age is not None or city is not None:
		employees_filter = list(filter(lambda x: (first_name is None or x['first_name'] == first_name) and
												 (age is None or x['age'] == age) and
												 (city is None or x['city'] == city), employees))

		return {"employees": employees_filter}
	return {"employees": employees}


@app.get("/employees/{employee_id}", status_code=status.HTTP_200_OK)
async def get_employee(employee_id: int):
	employee = list(filter(lambda x: x['id'] == employee_id, employees))
	if employee:
		return {"employee": employee[0]}
	else:
		raise HTTPException(status_code=404, detail="Сотрудник с таким id не существует")


@app.post("/employees/", response_model=Employee, status_code=status.HTTP_201_CREATED)
async def create_employee(employee: Employee) -> Any:
	if not all([employee.id != el["id"] for el in employees]):
		raise HTTPException(status_code=500, detail="Сотрудник с таким id уже существует")
	employees.append(employee.model_dump())
	return employee


@app.put("/employees/{employee_id}", status_code=status.HTTP_201_CREATED)
def update_item(employee_id: int, employee: Employee):
	employee_finded = list(filter(lambda x: employee.id == x["id"], employees))
	if len(employee_finded) == 0:
		raise HTTPException(status_code=404, detail="Сотрудник с таким id не существует")
	ind_emp = employees.index(employee_finded[0])
	employee_edit = employees.pop(ind_emp)
	employee_edit.update(employee.model_dump())
	employees.append(employee_edit)
	return {"employee_id": employee_id, "updated_data": employee_edit}


