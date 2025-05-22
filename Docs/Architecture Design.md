# Diseño de Arquitectura - Useit Library

## Backend: Arquitectura y Organización

### Framework y Lenguaje
El backend de Useit Library está desarrollado con **Django** y utiliza el patrón **MVC tradicional** más común en proyectos Django.

### Estructura del backend
El proyecto Django se organiza con múltiples apps según la responsabilidad funcional. Cada app contiene sus propios modelos, vistas, serializadores, servicios y rutas:

- `users`: Gestión de usuarios y roles
- `books`: Gestión de libros
- `loans`: Registro de préstamos y devoluciones

Cada app puede incluir:

- `models.py`: definición del modelo de datos
- `serializers.py`: serialización y validación de datos
- `views.py`: vistas basadas en clases con DRF
- `services.py`: lógica de negocio desacoplada
- `urls.py`: rutas específicas por módulo

### Roles y Permisos
- **Administrador**: puede crear, editar y eliminar libros.
- **Usuario regular**: puede listar libros, ver detalles y tomar o devolver préstamos.

Los permisos se gestionan a través de roles definidos en el modelo `User` y verificados en las vistas.

### Validaciones y Documentación de API
- Las validaciones se hacen desde los `serializers` de DRF.
- La documentación de la API se puede realizar mediante herramientas como Postman, como se solicita en la prueba.

---

## Frontend: Organización

### Lenguaje y Librerías
El frontend está construido usando **HTML y CSS con Bootstrap**, según lo requerido en la prueba.

### Diseño y Responsividad
- Se utiliza **Bootstrap** para garantizar una interfaz profesional y responsiva.
- Las vistas están organizadas por plantillas HTML en carpetas por módulo (`templates/books`, `templates/users`, etc.).

---

## Base de Datos

### Motor
La base de datos usada en producción y desarrollo es **PostgreSQL**.

### Estructura
Se implementan tres entidades principales basadas en el diagrama ER:

- **Book**: título, autor, año de publicación, stock
- **User**: nombre, correo, rol
- **Loan**: entidad intermedia que registra préstamos, fechas y devoluciones

---

## Estructura del Repositorio

```plaintext
main                # Rama protegida para lanzamientos estables
│
├── development     # Rama principal de desarrollo
│   ├── front       # Código del frontend (HTML, CSS, Bootstrap)
│   └── back        # Código del backend Django
│
├── docs            # Documentación técnica y Postman
└── database        # Scripts, migraciones y esquemas ER
