document.addEventListener('DOMContentLoaded', () => {
  const bookId = getBookIdFromUrl();
  if (bookId) {
    loadBookDetail(bookId);
  } else {
    showError("Invalid book ID.");
  }
});

function getBookIdFromUrl() {
  const parts = window.location.pathname.split('/');
  return parts[parts.length - 2]; // assumes URL ends with /<id>/
}

function loadBookDetail(id) {
  axios.get(`/api/books/${id}/`)
    .then(response => {
      const book = response.data;
      renderBook(book);
    })
    .catch(error => {
      showError("Book not found.");
      console.error(error);
    });
}

function renderBook(book) {
  const container = document.getElementById('book-detail');
  container.innerHTML = `
    <h2>${book.title}</h2>
    <p><strong>Author:</strong> ${book.author}</p>
    <p><strong>Year:</strong> ${book.publication_year}</p>
    <p><strong>Stock available:</strong> ${book.stock}</p>
  `;
}

function showError(message) {
  const container = document.getElementById('book-detail');
  container.innerHTML = `<div class="alert alert-danger">${message}</div>`;
}
