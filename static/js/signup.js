const form = document.querySelector('form');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    const newForm = new FormData(form);
    const formObj = Object.fromEntries(newForm);
    const json = JSON.stringify(formObj);

    fetch('/submitProfile', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: json
    })
});