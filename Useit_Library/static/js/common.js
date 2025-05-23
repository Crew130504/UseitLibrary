document.addEventListener('DOMContentLoaded', updateNavbarByRole);

function updateNavbarByRole() {
  const token = localStorage.getItem('access');
  const authContainer = document.getElementById('auth-buttons');
  const roleContainer = document.getElementById('user-role-button');

  if (!token) return;

  axios.get('/api/users/me/', {
    headers: { Authorization: `Bearer ${token}` }
  })
  .then(response => {
    const role = response.data.role;

    if (authContainer) {
      authContainer.remove();
    }

    let roleButton = '';
    if (role === 'admin') {
      roleButton = `<a href="/api/books/management/" class="btn btn-light me-2">Management</a>`;
    } else if (role === 'regular_user') {
      roleButton = `<a href="/api/loans/loan_template/" class="btn btn-warning me-2" style="background-color: #F4B400;">Loan</a>`;

    }

    const logoutButton = `<button onclick="logout()" class="btn btn-outline-light">Logout</button>`;

    roleContainer.innerHTML = roleButton + logoutButton;
    roleContainer.style.display = 'flex';
  })
  .catch(error => {
    console.warn('User role fetch failed:', error);
  });
}

function logout() {
  localStorage.removeItem('access');
  localStorage.removeItem('refresh');
  window.location.href = '/';
}
