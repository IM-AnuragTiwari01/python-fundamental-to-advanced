# file = open("order.txt", "w") # loaded that file to the mene=mory from disk
# try:
#     file.write("Masala Chai - 2 cups")
# finally:
#     file.close()


# -----------Modern Way--------------------
#  In this way we dont need to wrap the code in try except it automatically wraps everything

with open("orders.txt", "w") as file:
    file.write("ginger tea - 4 cups")