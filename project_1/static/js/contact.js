document.querySelector('.contact-form').addEventListener('submit', function (event) {
    event.preventDefault();  // Prevent form from submitting by default
    
    // Simple validation (can be improved)
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const subject = document.getElementById('subject').value;
    const message = document.getElementById('message').value;

    if (name && email && subject && message) {
        alert('Thank you for your message! We will get back to you soon.');
    } else {
        alert('Please fill in all fields.');
    }
});
