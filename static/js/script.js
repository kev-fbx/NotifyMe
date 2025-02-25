function transferData() {
  fetch('/readPTV', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
  })
  .then(response => response.json())
  .then(data => {
      alert(data.message);
  })
  .catch(error => {
      console.error('Error:', error);
      alert("An error occurred during transfer.");
  });
}