tea_size = input("> enter the cup size:").lower()
if tea_size == "small":
    print(" ₹10 ")
elif tea_size == "medium":
    print(" ₹15 ")
elif tea_size == "large":
    print(" ₹20 ")
else:
    print("Unavailable cup size")

