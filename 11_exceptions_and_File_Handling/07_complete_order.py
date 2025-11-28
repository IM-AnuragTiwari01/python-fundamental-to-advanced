# here we are going to develop a bill app where generate bill with all
# precautionary methods we have

class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"masala": 20, "ginger": 40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("That chai is not available")
        if not isinstance(cups, int): # isinstance() : function in python used to check if an object is an instance of a specific class or type, or subclass thereof.
            raise TypeError("Number of cups must be an integer")
        total = menu[flavor] * cups
        print(f"Your bill for { cups } cups of { flavor } chai: rupee { total }")

    except Exception as e:
        print("Error: ", e)
    finally:
        print("Thank You For Visiting ChaiCode")

print("-------------------------------")
bill("mint", 2)
print("-------------------------------")

bill("masala", "three")
print("-------------------------------")

bill("ginger", 3)
print("-------------------------------")

