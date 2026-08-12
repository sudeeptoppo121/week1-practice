def calculation_bill(price, quantity):
    total = price * quantity

# apply a discount of 10% if the total is greater than $100
    if total >= 200:
        discount = total * 0.10
        total = total - discount
    else:
        discount = 0

    final_amount = total - discount
    return total, discount, final_amount

#input section
product_name = input("Enter the product name: ")
price = float(input("Enter the price of the product: "))
quantity = int(input("Enter the quantity: "))

#call function
total_amount, discount, final_amount = calculation_bill(price, quantity)

#display the bill
print("\n--- Bill Summary ---") 
print(f"Product Name: {product_name}")
print(f"Price: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total Amount: ${total_amount:.2f}")
print(f"Discount: ${discount:.2f}")
print(f"Final Amount: ${final_amount:.2f}")
