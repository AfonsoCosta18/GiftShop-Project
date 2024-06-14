async function fetchProducts() {
    try {
        return await fetchJSON('/api/products');
    } catch (error) {
        console.error('Failed to fetch products:', error);
        displayErrorMessage('Failed to load products. Please try again later.');
    }
}

async function renderAdminProducts() {
    const products = await fetchProducts();
    if (!products) return;

    const container = document.getElementById('admin-products');
    container.innerHTML = '';
    products.forEach(p => {
        const productDiv = document.createElement('div');
        const productName = document.createElement('h3');
        productName.textContent = p.name || 'No Name';

        const productPrice = document.createElement('p');
        productPrice.textContent = `Price: $${p.price}`;

        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.onclick = () => deleteProduct(p.id);

        productDiv.appendChild(productName);
        productDiv.appendChild(productPrice);
        productDiv.appendChild(deleteButton);
        container.appendChild(productDiv);
    });
}

async function deleteProduct(productId) {
    try {
        await deleteJSON(`/api/products/${productId}`);
        alert(`Product ${productId} deleted!`);
        renderAdminProducts();
    } catch (error) {
        console.error(`Failed to delete product ${productId}:`, error);
        displayErrorMessage(`Failed to delete product. Please try again.`);
    }
}

document.getElementById('product-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const form = event.target;
    const data = {
        name: form.name.value,
        price: form.price.value
    };

    console.log('Submitting product:', data);  // Log data to check if it's correct

    try {
        await postJSON('/api/products', data);
        alert('Product added successfully!');
        form.reset();
        renderAdminProducts();
    } catch (error) {
        console.error('Failed to add product:', error);
        displayErrorMessage('Failed to add product. Please try again.');
    }
});


document.addEventListener('DOMContentLoaded', renderAdminProducts);

function displayErrorMessage(message) {
    // Implement displaying error messages on the UI
    console.error(message);  // Placeholder for actual UI implementation
}
