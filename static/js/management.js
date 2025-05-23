document.addEventListener('DOMContentLoaded', () => {
  const token = localStorage.getItem('access');
  const content = document.getElementById('management-content');
  const error = document.getElementById('not-authorized');

  if (!token) {
    error.style.display = 'block';
    content.style.display = 'none';
    return;
  }

  axios.get('/api/users/me/', {
    headers: { Authorization: `Bearer ${token}` }
  })
    .then(response => {
      if (response.data.role === 'admin') {
        error.style.display = 'none';
        content.style.display = 'block';
        setupManagementEvents();
        loadBooks();
      } else {
        error.style.display = 'block';
        content.style.display = 'none';
      }
    })
    .catch(error => {
      console.error("Error fetching user info:", error);
      error.style.display = 'block';
      content.style.display = 'none';
    });
});

function setupManagementEvents() {
  document.getElementById('book-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const token = localStorage.getItem('access');

    const id = document.getElementById('book-id').value;
    const bookData = {
      title: document.getElementById('title').value,
      author: document.getElementById('author').value,
      publication_year: document.getElementById('publication_year').value,
      stock: document.getElementById('stock').value,
    };

    const config = {
      headers: { Authorization: `Bearer ${token}` }
    };

    const url = id
      ? `/api/books/${id}/update/`
      : `/api/books/create/`;

    const method = id ? axios.put : axios.post;

    method(url, bookData, config)
      .then(() => {
        resetForm();
        loadBooks();
      })
      .catch(error => console.error('Save error:', error));
  });
}

function loadBooks() {
  axios.get('/api/books/data/')
    .then(response => {
      const books = response.data;
      const container = document.getElementById('book-list');
      container.innerHTML = '';

      books.forEach(book => {
        const col = document.createElement('div');
        col.className = 'col-md-4';
        col.innerHTML = `
          <div class="card p-3">
            <h5>${book.title}</h5>
            <p>${book.author} (${book.publication_year})</p>
            <p>Stock: ${book.stock}</p>
            <button class="btn btn-sm btn-primary me-2" onclick="editBook(${book.id})">Edit</button>
            <button class="btn btn-sm btn-danger" onclick="deleteBook(${book.id})">Delete</button>
          </div>
        `;
        container.appendChild(col);
      });
    })
    .catch(err => console.error('Error loading books:', err));
}

function editBook(id) {
  axios.get(`/api/books/${id}/`)
    .then(response => {
      const book = response.data;
      document.getElementById('book-id').value = book.id;
      document.getElementById('title').value = book.title;
      document.getElementById('author').value = book.author;
      document.getElementById('publication_year').value = book.publication_year;
      document.getElementById('stock').value = book.stock;
    })
    .catch(err => console.error('Error loading book:', err));
}

function deleteBook(id) {
  const token = localStorage.getItem('access');
  axios.delete(`/api/books/${id}/delete/`, {
    headers: { Authorization: `Bearer ${token}` }
  })
    .then(() => loadBooks())
    .catch(err => console.error('Delete error:', err));
}

function resetForm() {
  document.getElementById('book-form').reset();
  document.getElementById('book-id').value = '';
}
