# Entities – Useit Library

---

## Books

**Inclusion Rationale:**  
Represents the catalog of books available in the library. Each book can be loaned multiple times to different users. Availability is controlled via the `stock` field.

**Attributes:**
- `id` (Serial, Primary Key): Unique identifier of the book.
- `title` (String): Title of the book.
- `author` (String): Author of the book.
- `publication_year` (Integer): Year the book was published.
- `stock` (Integer): Number of available copies. Cannot be negative.

---

## Users

**Inclusion Rationale:**  
Manages the system's users, including both regular users (who can borrow books) and administrators (who manage the inventory).

**Attributes:**
- `id` (Serial, Primary Key): Unique identifier of the user.
- `name` (String): Full name of the user.
- `email` (String, unique): User's email address.
- `role` (String): User role. Can be `'regular_user'` or `'admin'`.

---

## Loans

**Inclusion Rationale:**  
Records every instance of a user borrowing a book. Acts as an intermediate table between `users` and `books`, enabling a complete loan and return history.

**Attributes:**
- `id` (Serial, Primary Key): Unique identifier of the loan.
- `user_id` (Integer, Foreign Key to `users.id`): User who borrowed the book.
- `book_id` (Integer, Foreign Key to `books.id`): Borrowed book.
- `loan_date` (Timestamp): Date when the book was borrowed.
- `return_date` (Timestamp, optional): Date when the book was returned.

---

## Relationships

**Users ↔ Loans ↔ Books**  
**Type:** One-to-many relationships.  
**Description:**
- A user can have multiple loans.  
- A book can be loaned multiple times.  
- Each loan is linked to a single user and a single book.  
**Implementation:**
The many-to-many relationship between `users` and `books` is implemented through the `loans` entity, which stores additional metadata such as dates.