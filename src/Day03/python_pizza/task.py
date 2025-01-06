from time import process_time

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

total_price = 0.0

def add_pepperoni_cost():
    if pepperoni.upper() == "Y":
        if size.upper() == "S":
            return 2
        elif size.upper() == "M" or size.upper() == "L":
            return 3
    return 0

def add_extre_cheese_cost():
    if extra_cheese.upper() == "Y":
        if size.upper() == "S" or size.upper() == "M" or size.upper() == "L":
            return 1
    return 0


if size.upper() == "S":
    total_price += 15
elif size.upper() == "M":
    total_price += 20
elif size.upper() == "L":
    total_price += 25
else:
    print("You have choosen an invalid size!")

total_price += add_pepperoni_cost()
total_price += add_extre_cheese_cost()

print(f"Your final bill is: ${int(total_price)}")



