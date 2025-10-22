// FunTime Ordering System - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
    loadProducts();
});

function loadProducts() {
    fetch('/products')
        .then(response => response.json())
        .then(data => {
            const grid = document.getElementById('product-grid');
            // TODO: Render products
            console.log('Products loaded:', data);
        })
        .catch(error => {
            console.error('Error loading products:', error);
        });
}

function addToCart(productId) {
    // TODO: Implement cart functionality
    console.log('Added product to cart:', productId);
}
