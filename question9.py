class Product:

    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

    def is_bulk_order(self):
        return self.quantity >= 10

    def __str__(self):
        return f"Product: {self.product_name} | Price: ₹{self.price:.2f} | Quantity: {self.quantity}"


# Input section
name = input("Enter Product Name: ")
price = float(input("Enter Price: "))
quantity = int(input("Enter Quantity: "))

# Create Object
product = Product(name, price, quantity)

# Determine order type
if product.is_bulk_order():
    order_type = "Bulk Order"
else:
    order_type = "Regular Order"

# Display section
print("\n--- Product Summary ---")
print(f"Product Name: {product.product_name}")
print(f"Price: ₹{product.price:.2f}")
print(f"Quantity: {product.quantity}")
print(f"Total Amount: ₹{product.calculate_total():.2f}")
print(f"Order Type: {order_type}")