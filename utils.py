"""
Utility functions for FunTime ordering system
"""

def format_price(amount):
    """Format price to 2 decimal places with currency symbol"""
    return f"${amount:.2f}"


def validate_email(email):
    """Basic email validation"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def generate_order_id():
    """Generate unique order ID"""
    import uuid
    return str(uuid.uuid4())[:8].upper()


def calculate_tax(subtotal, tax_rate=0.10):
    """Calculate tax amount"""
    return subtotal * tax_rate


def get_order_status_label(status):
    """Return human-readable order status"""
    status_labels = {
        'pending': 'Pending',
        'processing': 'Processing',
        'shipped': 'Shipped',
        'delivered': 'Delivered',
        'cancelled': 'Cancelled'
    }
    return status_labels.get(status, 'Unknown')
