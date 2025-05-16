# 📚 Book Recreate API

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-brightgreen)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A RESTful API built with **FastAPI** for managing books and users. This project demonstrates clean architecture, CRUD operations, Pydantic validation, and Swagger UI documentation.

---

## 🚀 Features

- Create, retrieve, and delete users
- Create, retrieve, and delete books
- Input validation using **Pydantic**
- Auto-generated interactive docs via **Swagger UI**
- Fully tested using **pytest**
- Modular folder structure

---

## 📦 Tech Stack

- Python 3.11+
- FastAPI
- Pydantic v2
- Starlette
- Pytest

---

## ⚙️ Setup

1. **Clone the repository:**

   git clone https://github.com/onovae/book_recreate.git
   cd book_recreate


2. **Create a virtual environment & activate it**
python -m venv venv

## # On Windows:
venv\Scripts\activate
## # On macOS/Linux:
source venv/bin/activate


3. **Install dependencies:**
pip install -r requirements.txt

4. **Run the API:**
## 
# Use uvicorn directly:
uvicorn main:app --reload
## # Or as a module:
python -m uvicorn main:app --reload


5. **Visit Swagger UI:**
Go to: http://127.0.0.1:8000/docs


6. **Run Tests:**
pytest


## Project Structure

book_recreate/
│
├── main.py              # Entry point
├── models/              # Pydantic models
├── services/            # Business logic
├── routers/             # API routes
├── test_app/            # Unit tests
├── requirements.txt     # Dependencies
└── README.md            # Project documentation


## 👨‍💻 Author
Built with ❤️ by Maureen Onovae and code in FastAPI.

*Feel free to contribute, raise issues, or suggest improvements.*
