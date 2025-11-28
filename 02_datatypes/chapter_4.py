is_boiling = True
#  True - represented as 1
#  False - represented as 0
stir_count = 5
total_actions = stir_count + is_boiling # UP-CASTING
print(f" total asctions: {total_actions}")

milk_present = 0 # no mmilk
#  we can print it in a boolean format
print(f"is there milk? {bool(milk_present)}")



water_hot = True
tea_added = True
can_serve = water_hot and tea_added
print(f"Can serve the Chai?: {can_serve}")

