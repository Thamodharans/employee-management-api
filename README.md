# employee-management-api

# Employee Management API (Django REST Framework)

#Project Overview
This project is a RESTful Employee Management API built using Django and Django REST Framework.

It supports full CRUD operations with:
- JWT Authentication
- Pagination
- Filtering
- Search
- Validation
- Admin Panel
- Automated Tests

---

#Tech Stack
- Python 3.x
- Django 4.x
- Django REST Framework
- Simple JWT
- SQLite (can be replaced with PostgreSQL)

---

#Features
- Create Employee
- List Employees (Paginated)
- Retrieve Single Employee
- Update Employee
- Delete Employee
- Filter by department and role
- Search by name and email
- JWT Authentication
- Admin panel
- Unit tests

---

#API Endpoints
- POST     /api/employees/ – Create employee  
- GET      /api/employees/ – List employees  
- GET      /api/employees/{id}/ – Retrieve employee  
- PUT      /api/employees/{id}/ – Update employee  
- DELETE   /api/employees/{id}/ – Delete employee  
- POST     /api/token/ – Get JWT token  
- POST     /api/token/refresh/ – Refresh JWT token  


---

#Authentication
Uses JWT authentication.  
Include token in headers:

---

#Setup Instructions

git clone https://github.com/your-username/employee-management-api.git
cd employee_api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

http://127.0.0.1:8000/admin/
python manage.py test
