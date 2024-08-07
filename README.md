# Django tasks CRUD with authentication

A Python application that provides a CRUD interface for tasks with user authentication system.
<br /><br />

## Features

- **User Authentication**: Sign up, log in, and manage user accounts.
- **Task Management**: Create, view, update, and delete tasks.
- **User-specific Data**: Each user can manage their own tasks.

## Made with
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" /> <img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" /> <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" />

## Installation

1. **Clone the Repository**
```bash
git clone https://github.com/MauroTDC/django_auth_crud.git
cd tasks_crud
```
2. **Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. **Install Dependencies**
```bash
pip install -r requirements.txt
```
4. **Configure Database**
```bash
By default, the project is set to use SQLite. 
To use PostgreSQL, update the DATABASES setting in myproject/settings.py with your PostgreSQL credentials.
```
5. **Apply Migrations**
```bash
python manage.py migrate
```
6. **Createa Superuser**
```bash
python manage.py createsuperuser
```
7. **Run Development Server**
```bash
python manage.py runserver
```
Open your browser and navigate to http://127.0.0.1:8000/ to see the application in action.

## Usage
<ul>
<li>Register: Go to /signup/ to create a new user account.</li>
<li>Log In: Go to /signin/ to log in to your account.</li>
<li>Tasks Management:
  <ul>
    <li>Create Task: Go to /tasks/create/ to create a new task.</li>
    <li>View Tasks: Go to /tasks/ to view all your tasks.</li>
    <li>Update Task: Go to /tasks/<task_id>/ to update a task.</li>
    <li>Delete Task: Go to /tasks/<task_id>/ to delete a task.</li>
  </ul>
</li>
</ul>
  
## Author

[MauroTDC](https://github.com/MauroTDC)
