document.getElementById('register-form').addEventListener('submit', function (e) {
  e.preventDefault();

  const data = {
    username: document.getElementById('username').value,
    email: document.getElementById('email').value,
    password: document.getElementById('password').value,
  };

  axios.post('/api/users/registerAPI/', data)
    .then(response => {
      alert('Account created successfully!');
      window.location.href = '/api/users/login/';
    })
    .catch(error => {
      alert('Registration failed. Check your info.');
      console.error(error.response.data);
    });
});
