document.addEventListener('DOMContentLoaded', async () => {
    const products = await fetchJSON('/api/products');
    console.log('Fetched products:', products);
    const container = document.getElementById('products');
    container.innerHTML = products.map(p => `
        <div>
            <h2>${p.name || 'No Name'}</h2>
            <img src="${p.image_url}" alt="${p.name}" width="200" height="200">
            <p>Price: €${p.price}</p>
            <button onclick="addToCart(${p.id})">Add to Cart</button>
        </div>
    `).join('');
});

async function addToCart(productId) {
    console.log(`Adding product with ID: ${productId}`);
    try {
        const response = await fetch('/api/cart', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ productId: productId }),
        });

        if (response.ok) {
            alert('Product added to cart!');
        } else {
            const errorData = await response.json();
            alert(`Error: ${errorData.message}`);
        }
    } catch (error) {
        console.error('Error adding to cart:', error);
        alert('Error adding to cart. Please try again.');
    }
}

async function fetchJSON(url) {
    const response = await fetch(url);
    return response.json();
}
