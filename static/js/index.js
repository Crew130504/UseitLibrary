document.addEventListener('DOMContentLoaded', () => {
  loadBooks();
});

function loadBooks() {
  axios.get('/api/books/data/')
    .then(response => {
      const books = response.data;
      const container = document.getElementById('book-list');

      books.forEach(book => {
        const col = document.createElement('div');
        col.className = 'col-md-4';
        col.innerHTML = `
          <div class="card h-100">
            <div class="card-body">
              <h5 class="card-title">${book.title}</h5>
              <a href="/books/${book.id}/" class="btn btn-primary mt-2">View Details</a>
            </div>
          </div>
        `;
        container.appendChild(col);
      });
    })
    .catch(error => {
      console.error('Error loading books:', error);
    });
}
