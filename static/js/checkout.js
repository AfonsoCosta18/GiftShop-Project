document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/cart')
        .then(response => response.json())
        .then(data => {
            const checkoutForm = document.getElementById('checkout-form');
            const cartDiv = document.createElement('div');
            cartDiv.id = 'checkout-cart-items';
            
            data.cart.forEach(item => {
                const itemElement = document.createElement('div');
                itemElement.innerHTML = `
                    <h3>${item.name}</h3>
                    <p>Quantity: ${item.quantity}</p>
                `;
                cartDiv.appendChild(itemElement);
            });

            checkoutForm.insertBefore(cartDiv, checkoutForm.firstChild);
        })
        .catch(error => {
            console.error('Error fetching cart items:', error);
        });

    document.getElementById('checkout-form').addEventListener('submit', function(event) {
        event.preventDefault();

        // Get form data
        const formData = new FormData(this);
        const formObject = Object.fromEntries(formData.entries());

        fetch('/api/order', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formObject)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Show success message
                alert('Order placed successfully!');

                // Clear the cart
                fetch('/api/cart/clear', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        // Update the UI to remove cart items
                        const cartDiv = document.getElementById('checkout-cart-items');
                        if (cartDiv) {
                            cartDiv.innerHTML = '<p>Your cart is empty.</p>';
                        }
                    }
                })
                .catch(error => {
                    console.error('Error clearing cart:', error);
                });
            }
        })
        .catch(error => {
            console.error('Error placing order:', error);
        });
    });
});

//document.addEventListener('DOMContentLoaded', () => {
    //fetch('/api/cart')
        //.then(response => response.json())
        //.then(data => {
            //const checkoutForm = document.getElementById('checkout-form');
            //const cartDiv = document.createElement('div');
            //cartDiv.id = 'checkout-cart-items';
            
            //data.cart.forEach(item => {
                //const itemElement = document.createElement('div');
                //itemElement.innerHTML = `
                    //<h3>${item.name}</h3>
                    //<p>Quantity: ${item.quantity}</p>
                //`;
                //cartDiv.appendChild(itemElement);
            //});

            //checkoutForm.insertBefore(cartDiv, checkoutForm.firstChild);
        //})
        //.catch(error => {
            //console.error('Error fetching cart items:', error);
        //});
//});
