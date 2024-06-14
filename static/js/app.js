async function fetchJSON(url, options = {}) {
    try {
        const response = await fetch(url, options);
        if (!response.ok) {
            throw new Error('Failed to fetch data.');
        }
        const data = await response.json();
        console.log('Fetched data:', data); // Log the fetched data for debugging
        return data;
    } catch (error) {
        console.error('Error fetching data:', error);
        displayErrorMessage('Error fetching data. Please try again.');
        return null;
    }
}

async function postJSON(url, data) {
    return await fetchJSON(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
}

async function putJSON(url, data) {
    return await fetchJSON(url, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
}

async function deleteJSON(url) {
    return await fetchJSON(url, { method: 'DELETE' });
}

async function handleAddToCart(productId) {
    try {
        const product = await fetchJSON(`/api/products/${productId}`);
        console.log('Product to add:', product); // Log product details
        if (product) {
            addToCart(product);  // Ensure product object is passed correctly
        } else {
            displayErrorMessage('Product not found.');
        }
    } catch (error) {
        console.error('Error adding to cart:', error);
        displayErrorMessage('Error adding to cart. Please try again.');
    }
}

function addToCart(product) {
    const cart = getCart();
    console.log('Adding product:', product); //Log the product being added
    const existingItem = cart.find(item => item.id === product.id);
    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        product.quantity = 1;
        cart.push(product);
    }
    saveCart(cart);
    console.log('Cart updated:', cart); //Log the updated cart
    alert(`${product.name} added to cart!`);
}

function getCart() {
    return JSON.parse(localStorage.getItem('cart') || '[]');
}

function saveCart(cart) {
    localStorage.setItem('cart', JSON.stringify(cart));
}

function displayErrorMessage(message) {
    // Implement this function to show user-friendly error messages on the UI
    console.error(message);  // Placeholder for actual UI implementation
}
