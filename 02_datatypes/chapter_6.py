#string 

chai_type = "Ginger chai"
customer_name = "Priya"
print(f"Order for {customer_name} : {chai_type} please!")

chai_description = "Aromatic and Bold more"
 # we want the first and the last word
 #indexing part of the string

print(f"First word: {chai_description[0:8:1]}")
# str[x: y: z]  z-> indicates every zth character

print(f"Last word : {chai_description[13:]}")

print(f"Reversed String is : {chai_description[::-1]}")
revStr = chai_description[::-1]
print(f"reveersed string : {revStr}")

label_text = "Chai Special" 