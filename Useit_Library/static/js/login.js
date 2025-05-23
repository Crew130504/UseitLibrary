document.getElementById('login-form').addEventListener('submit', function (e) {
  e.preventDefault();

  const data = {
    username: document.getElementById('username').value,
    password: document.getElementById('password').value,
  };

  axios.post('/api/users/loginAPI/', data)
    .then(response => {
      localStorage.setItem('access', response.data.access);
      localStorage.setItem('refresh', response.data.refresh);
      alert('Login successful!');
      window.location.href = '/'; // redirect to index
    })
    .catch(error => {
      alert('Login failed. Check your credentials.');
      console.error(error.response.data);
    });
});
