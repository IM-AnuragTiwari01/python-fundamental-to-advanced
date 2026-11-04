# Scopes and Name Resolution                 |
# Local - inside a function                  | 
# Enclosing - from outer function if nested  |
# global - Top level script                  |
# built in                                   |
#--------------------------------------------|

def serve_chai():
    chai_type = "Masala" # local scope
    print(f"inside function: {chai_type}")
    
chai_type = "Lemon"
serve_chai()
print(f"outside function: {chai_type}")

def chai_counter():
    chai_order = "Lemon" # enclosing scope
    def print_order():
        chai_order = "Ginger"
        print(f"Inner: {chai_order}")
    print_order()
    print(f"Outer: {chai_order}")
    
chai_order = "Tulsi" # Global scope
chai_counter()
print(f"Global: {chai_order}")
