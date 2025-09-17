# Backend_-Django-_Assessment
Backend_(Django)_Assessment for Python Backend Developer (Intern) role at Raktch Technology & Software.

# Employee Management System

A Django-based backend system for managing employees, departments, and achievements.

## Features

- User authentication with email and password
- CRUD operations for employees
- Department and achievement management
- Many-to-many relationship between employees and achievements
- MYSQL database (Connected)

## Setup Instructions

1. Clone the repository:
bash
git clone <repository-url>

2. Create a virtual environment and activate it:
- python -m venv venv
- source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
# Install Django
- pip install django

4. Run migrations:
# cd employee_management
- python manage.py makemigrations
- python manage.py migrate

5. Create a superuser (optional):
- python manage.py createsuperuser

6. Run the development server:
-  python manage.py runserver
