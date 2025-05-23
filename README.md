# Useit Library

This is a Django-based library management system, implementing user authentication, book management, borrowing, and returning functionalities.

## Features

* Book listing and detail views
* Admin-only book management (create, edit, delete)
* User roles: "regular user" and "administrator"
* Borrow and return books functionality
* REST API built with Django REST Framework
* Postman API collection for testing
* ✅ Live deployment on [Render](https://useitlibrary.onrender.com)

## Technologies Used

* Django
* Django REST Framework
* PostgreSQL
* Bootstrap (frontend)
* Render (cloud deployment)

## Setup Instructions

### Prerequisites

* Python 3.x
* Git
* PostgreSQL

### Installation

Clone the repository:

```bash
git clone <your-repo-url>
cd UseitLibrary
````

### Windows Automated Setup Script

Save this script as `setup_and_run.bat`:

```batch
@echo off

REM Create and activate virtual environment
python -m venv venv
call venv\Scripts\activate

REM Install dependencies
pip install -r requirements.txt

REM Prompt for environment variables
set /p SECRET_KEY="Enter your SECRET_KEY: "
set /p DATABASE_URL="Enter your DATABASE_URL: "

echo SECRET_KEY=%SECRET_KEY% > .env
echo DATABASE_URL=%DATABASE_URL% >> .env

REM Apply migrations and create superuser
python manage.py migrate
python manage.py createsuperuser

REM Run the application
python manage.py runserver
pause
```

Run the script by double-clicking the `setup_and_run.bat` file or executing it from the command prompt.

### Manual Setup

Set up a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure environment variables in `.env` file:

```env
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
```

Apply migrations:

```bash
python manage.py migrate
```

Create superuser:

```bash
python manage.py createsuperuser
```

### Run the Application Locally

Start the server:

```bash
python manage.py runserver
```

Access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## 🌐 Deployment

This application is live at:
👉 **[https://useitlibrary.onrender.com](https://useitlibrary.onrender.com)**

Deployment is done using Render with automatic GitHub deploys and environment variables configured in the dashboard.

---

## API Usage

The REST API endpoints are available at `/api/`.
Detailed documentation and test cases are provided in the Postman collection JSON file (`Useit Library API.json`).
