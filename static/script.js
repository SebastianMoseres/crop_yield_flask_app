// static/script.js

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('prediction-form');
    const resultContainer = document.getElementById('result-container');

    form.addEventListener('submit', function(event) {
        // Prevent the default form submission (which causes a page reload)
        event.preventDefault();

        // Show a loading message
        resultContainer.innerHTML = '<div class="prediction">Calculating...</div>';

        // Collect the form data
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        // Send the data to the Flask API using the fetch() function
        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json()) // Parse the JSON response from the server
        .then(result => {
            // Update the result container with the prediction
            const predictionText = `Predicted Crop Yield: <strong>${result.prediction.toFixed(2)} tons per hectare</strong>`;
            resultContainer.innerHTML = `<div class="prediction">${predictionText}</div>`;
        })
        .catch(error => {
            // Handle any errors that occurred during the fetch
            console.error('Error:', error);
            resultContainer.innerHTML = '<div class="prediction" style="background-color: #ffdddd; border-left-color: #d32f2f;">An error occurred. Please try again.</div>';
        });
    });
});