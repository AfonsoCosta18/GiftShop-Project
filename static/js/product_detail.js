document.addEventListener('DOMContentLoaded', async () => {
    const productId = window.location.pathname.split('/').pop();
    const product = await fetchJSON(`/api/products/${productId}`);
    const container = document.getElementById('product-details');
    container.innerHTML = `
        <h2>${product.name || 'No Name'}</h2>
        <p>Price: $${product.price}</p>
        <button onclick="addToCart(${product.id})">Add to Cart</button>
    `;
});

function addToCart(productId) {
    fetchJSON(`/api/products/${productId}`)
        .then(product => {
            addToCart(product);
        })
        .catch(error => {
            alert('Error adding to cart: ' + error.message);
        });
}
