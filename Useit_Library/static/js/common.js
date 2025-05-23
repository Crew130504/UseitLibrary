function getToken() {
  return localStorage.getItem('access');
}

function setToken(token) {
  localStorage.setItem('access', token);
}

function isAuthenticated() {
  return !!getToken();
}

function logout() {
  localStorage.removeItem('access');
  window.location.href = 'login.html';
}
