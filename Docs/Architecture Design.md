
# Architecture Design - Useit Library

## Backend: Architecture and Organization

### Framework and Language
The backend of Useit Library is developed using **Django** and follows the **traditional MVC pattern** commonly used in Django projects.

### Backend Structure
The Django project is organized into multiple apps based on functional responsibility. Each app contains its own models, views, serializers, services, and routes:

- `users`: User and role management
- `books`: Book management
- `loans`: Loan and return registration

Each app may include:

- `models.py`: data model definitions
- `serializers.py`: data serialization and validation
- `views.py`: class-based views using DRF
- `services.py`: decoupled business logic
- `urls.py`: module-specific routes

### Roles and Permissions
- **Administrator**: can create, edit, and delete books.
- **Regular User**: can list books, view details, and borrow or return books.

Permissions are managed through roles defined in the `User` model and enforced in views.

### Validation and API Documentation
- Validations are handled by DRF `serializers`.
- API documentation can be generated using tools like Postman, as required in the test.

---

## Frontend: Structure

### Language and Libraries
The frontend is built using **HTML and CSS with Bootstrap**, as required by the test.

### Design and Responsiveness
- **Bootstrap** is used to ensure a professional and responsive UI.
- Responsive design is implemented using Bootstrap's grid system and components.
- `cards` are used to display books, `tables` for history, and consistent form styling.

### Frontend Structure
The frontend is located outside the Django backend folder and follows this structure:

```plaintext
frontend/
├── index.html                 # Main page displaying book listings
├── login.html                 # Login form
├── register.html              # User registration form
├── dashboard.html             # User dashboard for loan history and returns

├── css/                       # Stylesheets
│   ├── common.css             # Shared styles (navbar, layout, typography)
│   ├── index.css              # Styles for index.html
│   ├── login.css              # Styles for login.html
│   ├── register.css           # Styles for register.html
│   └── dashboard.css          # Styles for dashboard.html

├── js/                        # JavaScript files
│   ├── common.js              # Shared functions (JWT handling, helpers)
│   ├── index.js               # Fetch and render books in index.html
│   ├── login.js               # Authentication logic and token storage
│   ├── register.js            # Form validation and registration logic
│   └── dashboard.js           # Logic for viewing and returning loans

└── assets/                    # Static resources
    └── logo.png               # Logo or other image assets


### User Flow
1. The user accesses the login or registration page.
2. After authentication, the JWT token is stored in `localStorage`.
3. The user can view the list of available books.
4. The user can borrow a book.
5. The user accesses the dashboard to view history and return books.

---

## Database

### Engine
The database used in both production and development is **PostgreSQL**.

### Structure
Three main entities are implemented based on the ER diagram:

- **Book**: title, author, publication year, stock
- **User**: name, email, role
- **Loan**: intermediate entity that records loans, dates, and returns

---

## Repository Structure

```plaintext
main                # Protected branch for stable releases
│
├── development     # Main development branch
│   ├── front       # Frontend code (HTML, CSS, Bootstrap)
│   └── back        # Backend Django code
│       ├──feat/init-project
│       ├──feat/jwt
│       ├──feat/models
│       ├──feat/serializers
│       └──feat/views
└── docs            # Technical documentation and Postman collection
```