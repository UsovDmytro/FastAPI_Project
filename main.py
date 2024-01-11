from fastapi import FastAPI, Query
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
    {"first_name": "John",
     "last_name": "Doe",
     "date_joined": date(2020, 5, 15),
     "age": 28,
     "city": "New York",
     "library_id": 1,
     "is_active": True,
     "salary": 50000
     },
    {"first_name": "Jane",
     "last_name": "Smith",
     "date_joined": date(2019, 8, 23),
     "age": 35,
     "city": "Los Angeles",
     "library_id": 1,
     "is_active": False,
     "salary": 60000
     },
    {"first_name": "Bob",
     "last_name": "Johnson",
     "date_joined": date(2021, 3, 10),
     "age": 32, "city": "Chicago",
     "library_id": 2,
     "is_active": True,
     "salary": 55000
     },
    {"first_name": "Alice",
     "last_name": "Williams",
     "date_joined": date(2018, 12, 5),
     "age": 40,
     "city": "Houston",
     "library_id": 2,
     "is_active": False,
     "salary": 70000
     },
    {"first_name": "Charlie",
     "last_name": "Brown",
     "date_joined": date(2022, 7, 18),
     "age": 25,
     "city": "San Francisco",
     "library_id": 3,
     "is_active": True,
     "salary": 48000
     },
    {"first_name": "Eva",
     "last_name": "Davis",
     "date_joined": date(2020, 1, 30),
     "age": 29,
     "city": "Miami",
     "library_id": 3,
     "is_active": True,
     "salary": 52000
     },
    {"first_name": "David",
     "last_name": "Miller",
     "date_joined": date(2017, 6, 8),
     "age": 45,
     "city": "Seattle",
     "library_id": 3,
     "is_active": False,
     "salary": 75000
     },
    {"first_name": "Grace",
     "last_name": "Jones",
     "date_joined": date(2019, 11, 12),
     "age": 31,
     "city": "Dallas",
     "library_id": 4,
     "is_active": True,
     "salary": 58000
     },
    {"first_name": "Frank",
     "last_name": "Taylor",
     "date_joined": date(2023, 2, 25),
     "age": 26,
     "city": "Atlanta",
     "library_id": 4,
     "is_active": False,
     "salary": 63000
     },
    {"first_name": "Helen",
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




