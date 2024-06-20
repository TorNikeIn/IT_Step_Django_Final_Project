# Simple Web Cataloh Django CRUD App

This is a simple Django application for managing websites by categories. It demonstrates basic CRUD (Create, Read, Update, Delete) functionality for managing website entries.

## Features

- Add, edit, and delete websites.
- View websites filtered by categories.
- Each website is displayed in a card format with options to "Go To", "Edit", and "Delete".

## Getting Started

### Prerequisites

- Python 3.x
- Django 3.x or later

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/simple-django-crud-app.git
   cd simple-django-crud-app

Project Structure

simple-django-crud-app/
│
├── myapp/
│   ├── migrations/
│   ├── templates/
│   │   ├── add_category.html
│   │   ├── edit_website.html
│   │   ├── confirm_delete.html
│   │   ├── website_list.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│
├── simple_django_crud/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md


Usage
Add Categories:

Go to http://127.0.0.1:8000/admin/ and log in with the superuser credentials.
Add categories using the Django admin interface.
Add Websites:

Use the custom form at http://127.0.0.1:8000/categories/add/ to add new categories.
After adding categories, add websites to the respective categories.
Manage Websites:

View websites in their respective categories.
Use the "Go To" button to visit the website.
Use the "Edit" button to update website details.
Use the "Delete" button to remove the website.
