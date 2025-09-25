# Student_Exam_Portal_Django
A Django Project for student Exam Portal
 

A simple Student Exam Portal with registration, login, exam listing/registration, and viewing results. Built with Django for clarity and simplicity.

## Features
- User registration and login (basic validation)
- Protected pages: `Dashboard`, `Exams`, `Results`
- Register for available exams
- View results (marks/grade and admit card link)
- Success/error messages for login/register/logout

## Requirements
- Python 3.11+
- Django 5.2+

## Setup (Windows PowerShell)
```bash
# Create and activate venv
python -m venv venv
venv\Scripts\Activate.ps1

# Install dependencies
pip install django==5.2.6

# Migrate DB
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run server
python manage.py runserver
```
Visit `http://127.0.0.1:8000/`.

## Usage
- Register, then login.
- Use `Dashboard` to navigate to `Exams` and `Results`.
- In `Exams`, click Register to add a registration.
- View your registrations and marks in `Results`.

## Notes
- CSRF is enabled; all POST forms include `{% csrf_token %}`.
- Login redirect is configured via `LOGIN_URL = '/login/'`.
- To add exams, use Django Admin (`/admin/`) and create `Exam` entries.
