def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        cost = price * quantity
        print(f"total cost is {cost}")
    except KeyError:
        print("Sorry that chai not on memu")
    except TypeError:
        print("Quantity must be in number")



process_order("ginger", 2)
print("-------------------------------------")
process_order("masala", "two")