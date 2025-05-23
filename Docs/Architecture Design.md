# Architecture Design - Useit Library

## Backend: Architecture and Organization

### Framework and Language
The backend of Useit Library is developed using **Django** and follows the **MTV pattern** (Model-Template-View). It leverages **Django REST Framework** for building RESTful APIs.

### Backend Structure
The Django project is organized into three main apps based on functionality:

- `book`: book catalog and management
- `loan`: loan creation, return and history
- `user`: authentication and user profile management

Each app includes:

- `models.py`: ORM model definitions
- `serializers.py`: DRF serializers for validation and serialization
- `views.py`: API views and frontend-compatible views
- `permissions.py`: custom permission classes (in user app)
- `urls.py`: app-level routing
- `templates/`: HTML templates per module
- `tests.py`: unit tests for API and business logic

The `Useit_Library` root module handles project-level settings, routing and WSGI entry.

### JWT Authentication
JWT tokens are implemented using `rest_framework_simplejwt`.
- `TokenObtainPairView` for login
- `TokenRefreshView` for refreshing tokens
- All protected endpoints use `IsAuthenticated` along with role-based permissions (`IsAdminRole`, `IsRegularUser`).

### API Overview
- `POST /api/users/registerAPI/` — register user
- `POST /api/loginAPI/` — JWT login
- `GET /api/users/me/` — get current user info

- `GET /api/books/data/` — list books
- `GET /api/books/<id>/` — book details
- `POST /api/books/create/` — create book (admin)
- `PUT /api/books/<id>/update/` — update book (admin)
- `DELETE /api/books/<id>/delete/` — delete book (admin)

- `POST /api/loans/create/` — borrow book (user)
- `PUT /api/loans/return/<id>/` — return book (user)
- `GET /api/loans/history/` — view own loan history (user)

---

## Project Structure (File System)

```plaintext
UseitLibrary/
├── Docs/
│   ├── Diagrams/
│   │   ├── Diagram-ER.png
│   │   └── Diagram-UseCase.png
│   ├── Architecture Design.md
│   ├── Database.md
│   └── Useit Library API.json
│
├── Useit_Library/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── book/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── templates/book/
│       ├── detail.html
│       ├── index.html
│       └── management.html
│
├── loan/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── templates/loan/
│       └── loan.html
│
├── user/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── templates/user/
│       ├── dashboard.html
│       ├── login.html
│       └── register.html
│
├── static/
│   ├── assets/
│   ├── css/
│   └── js/
│
├── templates/
│   └── base.html
│
├── .env
├── .gitignore
├── LICENSE
├── README.md
├── manage.py
└── requirements.txt
```

---

## Repository Branches

```plaintext
main                # Stable branch           # Frontend isolated branch
├── deploy          # For deployment setup
├── development     # Development integration
    ├── back            # Backend isolated branch
    |   ├── feat/init-project
    |   ├── feat/jwt
    |   ├── feat/models
    |   ├── feat/serializers
    |   └──feat/views
    └──front
├── docs            # Markdown and Postman documentation

```

---
