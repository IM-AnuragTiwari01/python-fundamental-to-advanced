snack = input("> Enter the snack you want to have: ").lower()

if snack == "samosa" or snack == "cookies":
    print(f"Kindly wait confirming your order --> {snack}")
else:
    print(f"Requested item is unavailable")