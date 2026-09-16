order_amount = int(input("> Enter the amount: "))
delivery_fees = 0 if order_amount > 300 else 300
print(f"Delivery fees is: {delivery_fees}")