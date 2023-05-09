// For Sign In.
const form = document.getElementById('login-form');
const submitButton = document.querySelector('button[type="submit"]');

var messageBox = document.querySelector('.message');

form.addEventListener('submit', function (event) {
    event.preventDefault();
    handleFormSubmission();
})

function handleFormSubmission() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/login');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function () {
      
        if (xhr.status === 200) {
            window.location.href = '/';
        } else if (xhr.status === 401){
            const response = JSON.parse(xhr.responseText);
            messageBox.textContent = response.message;
        } else {
            messageBox.textContent = 'Error: ' + xhr.statusText;
        }
    };

    xhr.send(JSON.stringify({ username: username, password: password }));
}

// For Sign Up.
const form2 = document.getElementById('signup-form');
var submitButton2 = document.getElementsByClassName('submit-btn2')[0];
var messageBox2 = document.querySelector('.message2');

form2.addEventListener('submit', function (event) {
    event.preventDefault();
    handleFormSubmission2();
})

function handleFormSubmission2() {
    const first_name = document.getElementById('first_name').value;
    const last_name = document.getElementById('last_name').value;
    const username2 = document.getElementById('username2').value;
    const password2 = document.getElementById('password2').value;
    const email_id = document.getElementById('email_id').value;
    const mobile_number = document.getElementById('mobile_number').value;
    const dob = document.getElementById('dob').value;

    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/signup');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function () {
        if (xhr.status === 200) {
            window.location.href = '/';
        } else if (xhr.status === 401) {
            const response = JSON.parse(xhr.responseText);
            messageBox2.textContent = response.message;
        } else {
            messageBox2.textContent = 'Error: ' + xhr.statusText;
        }
    };

    xhr.send(JSON.stringify({ first_name: first_name, last_name: last_name, email_id: email_id, mobile_number: mobile_number, username2: username2, password2: password2, dob: dob }));
}