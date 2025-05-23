document.addEventListener('DOMContentLoaded', () => {
  const token = localStorage.getItem('access');
  const authSection = document.getElementById('loan-content');
  const errorSection = document.getElementById('not-authorized');

  if (!token) {
    errorSection.style.display = 'block';
    authSection.style.display = 'none';
    return;
  }

  axios.get('/api/users/me/', {
    headers: { Authorization: `Bearer ${token}` }
  })
  .then(response => {
    const user = response.data;
    console.log("User info:", user);

    if (user.role === 'regular_user') {
      errorSection.style.display = 'none';
      authSection.style.display = 'block';
      loadLoans();
      loadAvailableBooks();
    } else {
      errorSection.style.display = 'block';
      authSection.style.display = 'none';
    }
  })
  .catch(error => {
    console.error("Error fetching user info:", error);
    errorSection.style.display = 'block';
    authSection.style.display = 'none';
  });
});

function loadLoans() {
  const token = localStorage.getItem('access');

  axios.get('/api/loans/history/', {
    headers: { Authorization: `Bearer ${token}` }
  })
  .then(response => {
    const loans = response.data;
    const loanList = document.getElementById('loan-list');
    loanList.innerHTML = '';

    loans.forEach(loan => {
      const item = document.createElement('div');
      item.className = 'card p-3';
      item.innerHTML = `
        <p><strong>Book:</strong> ${loan.book.title}</p>
        <p><strong>Loan Date:</strong> ${new Date(loan.loan_date).toLocaleDateString()}</p>
        <p><strong>Status:</strong> ${loan.return_date ? 'Returned' : 'Active'}</p>
        ${!loan.return_date ? `<button class="btn btn-sm btn-primary" onclick="returnBook(${loan.id})">Return</button>` : ''}
      `;
      loanList.appendChild(item);
    });
  })
  .catch(error => {
    console.error('Error loading loans:', error);
  });
}

function loadAvailableBooks() {
  axios.get('/api/books/data/')
    .then(response => {
      const books = response.data;
      const bookContainer = document.getElementById('available-books');
      bookContainer.innerHTML = '';

      books.forEach(book => {
        const card = document.createElement('div');
        card.className = 'col-md-4';
        card.innerHTML = `
          <div class="card h-100 p-3">
            <h5>${book.title}</h5>
            <p><strong>Author:</strong> ${book.author}</p>
            <p><strong>Stock:</strong> ${book.stock}</p>
            <button class="btn btn-success" onclick="borrowBook(${book.id})" ${book.stock === 0 ? 'disabled' : ''}>Borrow</button>
          </div>
        `;
        bookContainer.appendChild(card);
      });
    })
    .catch(error => {
      console.error('Error loading books:', error);
    });
}

function borrowBook(bookId) {
  const token = localStorage.getItem('access');

  axios.post('/api/loans/create/', { book_id: bookId }, {
    headers: { Authorization: `Bearer ${token}`,
      'Content-Type': 'application/json' }
  })
  .then(() => {
    alert('Book borrowed successfully');
    loadLoans();
    loadAvailableBooks();
  })
  .catch(error => {
    console.error('Error borrowing book:', error);
    alert('Failed to borrow book');
  });
}

function returnBook(loanId) {
  const token = localStorage.getItem('access');

  axios.patch(`/api/loans/return/${loanId}/`, {}, {
    headers: { Authorization: `Bearer ${token}` }
  })
  .then(() => {
    alert('Book returned successfully');
    loadLoans();
    loadAvailableBooks();
  })
  .catch(error => {
    console.error('Error returning book:', error);
    alert('Failed to return book');
  });
}
