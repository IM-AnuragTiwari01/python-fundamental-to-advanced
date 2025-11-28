# integer 

black_tea_grams = 14
ginger_grams = 3

total = black_tea_grams + ginger_grams
print(f"Total grams of base tea : {total}")

remaining_tea = black_tea_grams - ginger_grams
print(f"Total grams of remaining tea : {remaining_tea}")

milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving: {milk_per_serving}") #gets the exact floating answer


total_tea_bag = 7
pots = 4
bags_per_pot = total_tea_bag // pots
print(f"whole tea bags per pot: {bags_per_pot}") #not worried what comes after decimal

total_cardimom_pods = 10
pods_per_cup = 3
leftover_pods = total_cardimom_pods % pods_per_cup
print(f"leftover cardimom pods: {leftover_pods}") 


# we want an exponential power

base_flavour_strength = 2
scale_factor = 3
powerful_flavour = base_flavour_strength ** scale_factor
print(f"powerful flavour: {powerful_flavour}")


total_tea_leaves_harvested = 1_000_000_000 # to improve the readability
print(f"total tea leaves harvested: {total_tea_leaves_harvested}")