document.getElementById('uploadForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const cropType = document.getElementById('cropType').value;
    const fileInput = document.getElementById('formFile').files[0];

    if (!cropType || !fileInput) {
        alert('Please select a crop type and upload an image.');
        return;
    }

    const formData = new FormData();
    formData.append('crop_type', cropType);
    formData.append('file', fileInput);

    fetch('http://localhost:8000/upload-image/', {
        method: 'POST',
        body: formData,
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('result-box').classList.remove('d-none');
            document.getElementById('prediction-result').innerText = `Prediction: ${data.predicted_disease}`;
        })
        .catch(error => console.error('Error:', error));
});
