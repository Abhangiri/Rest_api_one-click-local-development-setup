# Student CRUD REST API

A Flask-based REST API for managing student records. This project includes endpoints for creating, retrieving, updating, and deleting student records, along with a health check endpoint.

## Features
- Add a new student.
- Get all students.
- Get a student by ID.
- Update an existing student.
- Delete a student.
- Healthcheck endpoint (`/healthcheck`).

## Tech Stack
- **Language:** Python
- **Framework:** Flask
- **Database:** SQLite (default)

## Prerequisites
- Python 3.8+
- `pip` for dependency management

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Abhangiri/student-crud-api.git
   cd student-crud-api

2. **Create a virtual environment and activate it**
python -m venv .module

# Windows:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\.module\Scripts\activate


3. Install dependencies:

pip install -r requirements.txt


4. Set up your .env file:

FLASK_APP=run.py
FLASK_ENV=development
DATABASE_URI=mysql+pymysql://<username>:<password>@<host>:<port>/<database_name>


5. Initialize the database:

flask db init
flask db migrate -m "Initial migration"
flask db upgrade


6. Run the application:

flask run



Using the API

Access the API documentation at: http://127.0.0.1:5000/apidocs





