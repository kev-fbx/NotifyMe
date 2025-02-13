function processDB() {
    fetch('/process_DB', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
    })
    .then(response => response.json())
    .then(data => {
      if (data.status === 'success') {
        alert('Data processed successfully');
      } else {
        alert('Data processing failed');
      }
    })
    .catch(error => {
      console.error('Error:', error);
  });
}