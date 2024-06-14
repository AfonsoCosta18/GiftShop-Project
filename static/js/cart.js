document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/cart')
        .then(response => response.json())
        .then(data => {
            const cartDiv = document.getElementById('cart-items');
            data.cart.forEach(item => {
                const itemElement = document.createElement('div');
                itemElement.innerHTML = `
                    <h3>${item.name}</h3>
                    <p>Quantity: ${item.quantity}</p>
                `;
                cartDiv.appendChild(itemElement);
            });
        });
});

