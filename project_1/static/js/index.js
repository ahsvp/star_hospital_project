// Wait for the document to load
document.addEventListener('DOMContentLoaded', function() {
    // Button hover animation effect
    const buttons = document.querySelectorAll('.service-btn, .department-btn, .cta-btn');

    buttons.forEach(button => {
        button.addEventListener('mouseover', () => {
            button.style.boxShadow = '0px 0px 15px rgba(255, 0, 255, 0.7)';
        });
        button.addEventListener('mouseout', () => {
            button.style.boxShadow = 'none';
        });
    });
//

    // Scroll effect for fading in sections
    const fadeInSections = document.querySelectorAll('.service-card, .department-card, .about-content');

    window.addEventListener('scroll', () => {
        fadeInSections.forEach(section => {
            const sectionTop = section.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;

            if (sectionTop < windowHeight - 100) {
                section.style.transition = 'opacity 1s ease-in-out, transform 1s ease-in-out';
                section.style.opacity = 1;
                section.style.transform = 'translateY(0)';
            } else {
                section.style.opacity = 0;
                section.style.transform = 'translateY(50px)';
            }
        });
    });
});

// js of about.html
document.addEventListener('DOMContentLoaded', function () {
    const cards = document.querySelectorAll('.info-card');

    cards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'scale(1.05)';
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'scale(1)';
        });
    });
});

// js of doctor.html
// You can add interactive features, like a search function or filtering doctors
document.addEventListener('DOMContentLoaded', function() {
    console.log('Doctor page loaded');
});

// js of booking.html
// Add any client-side validation or functionality
document.addEventListener('DOMContentLoaded', function() {
    console.log('Booking page loaded');
});

//code for whatsapp function


// js of contact.html
// let messageCount = 0; // Initialize a counter

// document.querySelector('.contact-form form').addEventListener('submit', function (event) {
//     // Simple validation (can be improved)
//     const name = document.getElementById('name').value;
//     const email = document.getElementById('email').value;
//     const subject = document.getElementById('subject').value;
//     const message = document.getElementById('message').value;

//     if (name && email && subject && message) {
//         // Increment the message count
//         messageCount++;

//         // Print the current message count to the console
//         console.log(`Number of messages sent: ${messageCount}`);

//         // Show the popup message
//         const popup = document.getElementById('popup-message');
//         popup.textContent = 'Thank you for your message! We will get back to you soon.';
//         popup.classList.add('show'); // Add the show class to display the popup

//         // Hide the popup after 3 seconds
//         setTimeout(() => {
//             popup.classList.remove('show'); // Remove the show class to hide the popup
//         }, 3000);
//         console.log('Form submitted!'); // Test if the form submission is detected
//         console.log(popup.classList); // Check if 'show' class is added

//         // Reset the form fields after submission
//         document.querySelector('.contact-form form').reset(); // Reset the form
//     } else {
//         event.preventDefault();  // Prevent form submission if fields are empty
//         alert('Please fill in all fields.');
//     }
// });


// js of department.html
// You can add any interactive functionality here
document.addEventListener('DOMContentLoaded', function() {
    console.log('Department page loaded');
});

