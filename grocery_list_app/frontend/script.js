async function addItem() {
    const name = document.getElementById('name').value;
    const quantity = parseInt(document.getElementById('quantity').value);

    // Check if quantity is negative or zero
    if (quantity <= 0 || isNaN(quantity)) {
        alert('Please enter a valid positive quantity.');
        return;
    }

    const response = await fetch('/items/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name: name,
            quantity: quantity
        })
    });

    if (response.ok) {
        const newItem = await response.json();
        document.getElementById('items').innerHTML += `<li>${newItem.name} - ${newItem.quantity}</li>`;
    }
}
