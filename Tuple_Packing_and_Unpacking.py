def display_orders(orders):
    for order in orders:
        # Unpacking the tuple
        customer_name, product, quantity = order
        
        # Formatting the order details
        print(f"Customer: {customer_name} ordered {quantity} x {product}.")

# Sample order data
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
]

# Call the function to display orders
display_orders(orders)
