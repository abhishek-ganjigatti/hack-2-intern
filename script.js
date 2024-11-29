// Wait for the document to be ready
document.addEventListener("DOMContentLoaded", function() {
    const registerForm = document.getElementById("register-form");

    // Handle form submission for registration
    registerForm.addEventListener("submit", function(event) {
        event.preventDefault();  // Prevent the form from submitting the default way

        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        // Basic validation (just checking if fields are filled)
        if (email && password) {
            console.log("Form submitted:", { email, password });
            // Here you could add an AJAX request to send the data to the server
        } else {
            alert("Please fill in both fields.");
        }
    });

    // Example of interacting with the budget data (Pie chart)
    const pieChart = document.getElementById("pie-chart");
    if (pieChart) {
        // Example: Add an event listener to display more info when a chart is clicked
        pieChart.addEventListener("click", function() {
            alert("You clicked on the pie chart!");
        });
    }
});
