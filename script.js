// script.js

// Function to fetch recommendations from the backend
function getRecommendations() {
    const soilType = document.getElementById('soilType').value.toLowerCase();
    const climate = document.getElementById('climate').value.toLowerCase();
    const symptoms = document.getElementById('symptoms').value.toLowerCase();

    // Assuming the backend provides a REST API
    fetch('/get_recommendations', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            soil_type: soilType,
            climate: climate,
            symptoms: symptoms
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('cropRecommendation').textContent = `Recommended crops: ${data.crops}`;
        document.getElementById('soilAdvice').textContent = `Soil management advice: ${data.soil_advice}`;
        document.getElementById('diseaseDiagnosis').textContent = `Disease diagnosis: ${data.disease}`;

        const tipsList = document.getElementById('farmingTips');
        tipsList.innerHTML = ''; // Clear previous tips
        data.tips.forEach(tip => {
            const listItem = document.createElement('li');
            listItem.textContent = tip;
            tipsList.appendChild(listItem);
        });
    })
    .catch(error => console.error('Error:', error));
}
