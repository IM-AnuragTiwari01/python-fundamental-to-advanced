# real  numbers ->  i want to have precision

import sys
from fractions import Fraction  # deals with fractions 
from decimal import Decimal  # dealas with decimal numbers

ideal_temp = 95.5
current_temp = 95.49

print(f"ideal temp : {ideal_temp}")
print(f"current temp: {current_temp}")
print(f"difference in temperature: { ideal_temp - current_temp }")

print(sys.float_info)

# ------------in python complex numbers do exists ----------------