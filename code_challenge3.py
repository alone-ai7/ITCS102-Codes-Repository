name = input("Please enter your name: ")

type_of_item = input("Please enter the type of item: ")

isFragile = bool(input("Is the package fragile: "))

weight = float(input("How heavy is the product in kg: "))

distance = float(input("How far is the package: "))

is_Express = bool(input("Is the package express: "))

is_International = bool(input("Is the package international: "))

base_cost = weight * 2.50 + distance * 0.15

if weight <= base_cost and distance <= base_cost: 
	print("The base cost is", base_cost, "Therefore the product is Free")
else:
	print("Invalid weight and distance")

