#Global Freight Calculator

name = input("Enter your name: ")

type_of_item = input("Please enter the type of the item: ")

is_Fragile = input("Is the product fragile? Yes/No---> ")

weight = float(input("How heavy is the product in kilograms?---> "))

distance = float(input("Please enter the distance of the product in kilometer---> "))

is_Express = input("Is the package express? True/False---> ") == "True" #this is to check if user typed True
is_International = input("Is the package international? True/False---> ") == "True"


base_cost = (weight * 2.50) + (distance * 0.15)
f_weight = 2.0
f_distance = 100

#all conditions must be met in order to be free

if weight <= f_weight and distance <= f_distance and is_Express == False and is_International == False:
	print("The base cost is", base_cost, "The package qualifies as light, local, and standard, so the shipping is free!")

#if not, they will follow these standard prices

elif is_Express == True and is_International == True:
	Total = (base_cost * 1.40) + 50
	print("The total cost is", Total,"PHP", "\n")

elif is_Express or is_International and weight > 20:
	Total = (base_cost * 1.20) + 25
	print("The total cost is", Total,"PHP","\n")

elif weight > 30 or distance > 1000:
	Total = base_cost + 30
	print("The total cost is", Total,"PHP","\n")

else:
	Total = base_cost
	print("The total cost is", Total,"PHP","\n")

#User's Info
print("User: ", name)
print("Product: ", type_of_item)
print("Is this item/s fragile: ", is_Fragile)
print("Total Weight: ", weight, "kg")
print("Total distance: ", distance, "km")
print("Did you avail the Express Service: ", is_Express)
print("Is the item international: ", is_International)
