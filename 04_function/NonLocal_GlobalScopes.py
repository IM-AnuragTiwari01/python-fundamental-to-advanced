def update_order():
    chai_type = "Elaichi"
    def kitchen():
        # whenever we give nonlocal this mean just above 
        # or just iutside this scope
        nonlocal chai_type
        chai_type = "Kesar"
    kitchen()
    print(f"After Kitchen update chai_type = {chai_type}")
    
update_order()
