document.getElementById('nameInput').addEventListener('keyup', function() {
    const name = this.value;
    document.getElementById('response').innerText = `Hello, ${name}!`;
});

document.getElementById('userForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const name = document.getElementById('nameInput').value;
    const age = document.getElementById('ageInput').value;
    
    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, age }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerHTML = `
            <p>Hello, ${name}! ${data.message}</p>
        `;
    });
});
