"""
FunTime Online Ordering System
Main application file
"""

from flask import Flask, render_template, request, jsonify
from models import Product, Order, OrderItem

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'

# Temporary in-memory storage (will move to database later)
products = []
orders = []


@app.route('/')
def index():
    """Homepage - display product catalog"""
    return render_template('index.html', products=products)


@app.route('/products')
def get_products():
    """API endpoint to fetch all products"""
    # TODO: Fetch from database
    return jsonify({'products': products})


@app.route('/cart')
def cart():
    """Shopping cart page"""
    return render_template('cart.html')


@app.route('/admin')
def admin_dashboard():
    """Admin panel for managing products and orders"""
    # TODO: Add authentication
    return render_template('admin.html', orders=orders)


@app.route('/api/order', methods=['POST'])
def create_order():
    """Process new order"""
    data = request.json
    # TODO: Validate order data
    # TODO: Save to database
    # TODO: Send confirmation email
    return jsonify({'success': True, 'message': 'Order placed successfully'})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
