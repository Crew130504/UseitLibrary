Entidades – Useit Library
Libros
Razón de inclusión:
Representa el catálogo de libros disponible en la biblioteca. Cada libro puede ser prestado múltiples veces a diferentes usuarios. Se controla la disponibilidad mediante el campo de stock.

Atributos:

id (Serial, Clave primaria): Identificador único de cada libro.

title (Cadena de texto): Título del libro.

author (Cadena de texto): Autor del libro.

publication_year (Entero): Año de publicación.

stock (Entero): Cantidad de ejemplares disponibles. No puede ser negativo.

Usuarios
Razón de inclusión:
Gestiona los usuarios del sistema, incluyendo tanto usuarios regulares (que pueden tomar libros prestados) como administradores (que gestionan el inventario).

Atributos:

id (Serial, Clave primaria): Identificador único del usuario.

name (Cadena de texto): Nombre completo del usuario.

email (Cadena de texto, único): Correo electrónico del usuario.

role (Cadena de texto): Rol del usuario. Puede ser 'regular_user' o 'admin'.

Préstamos
Razón de inclusión:
Registra cada vez que un usuario toma un libro prestado. Actúa como tabla intermedia entre users y books, permitiendo un historial completo de préstamos y devoluciones.

Atributos:

id (Serial, Clave primaria): Identificador único del préstamo.

user_id (Entero, Clave foránea a users.id): Usuario que realiza el préstamo.

book_id (Entero, Clave foránea a books.id): Libro prestado.

loan_date (Timestamp): Fecha en que se prestó el libro.

return_date (Timestamp, opcional): Fecha en que el libro fue devuelto.

Relaciones
Usuarios ↔ Préstamos ↔ Libros
Tipo: Relaciones uno a muchos.
Descripción:

Un usuario puede tener múltiples préstamos.

Un libro puede ser prestado múltiples veces.

Cada préstamo está asociado a un único usuario y un único libro.
Implementación:
La relación muchos a muchos entre users y books se resuelve mediante la entidad loans, que almacena datos adicionales como fechas.