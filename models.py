"""
Database models for FunTime ordering system
"""

from datetime import datetime

class Product:
    """Product model for catalog items"""
    def __init__(self, id, name, description, price, category, stock):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.stock = stock
        self.created_at = datetime.now()
    
    def __repr__(self):
        return f'<Product {self.name}>'


class Order:
    """Order model for customer purchases"""
    def __init__(self, id, customer_name, customer_email, total, status='pending'):
        self.id = id
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.total = total
        self.status = status
        self.created_at = datetime.now()
    
    def __repr__(self):
        return f'<Order {self.id}>'


class OrderItem:
    """Individual items within an order"""
    def __init__(self, order_id, product_id, quantity, price):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
    
    def get_subtotal(self):
        return self.quantity * self.price
