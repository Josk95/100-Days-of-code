
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

generated_password_list = []
password = ""
for num in range(0,nr_letters):
    generated_password_list.append(random.choice(letters))

for num in range(0,nr_symbols):
    generated_password_list.append(random.choice(symbols))

for num in range(0,nr_numbers):
    generated_password_list.append(random.choice(numbers))

print(f"Generated password list \n {generated_password_list}")

#Shuffle the generated password 3 times
for num in range(0,3):
    random.shuffle(generated_password_list)

print(f"3 times shuffled generated password list \n {generated_password_list}")

for char in generated_password_list:
    password += char

print(f"Your generated password is: {password}")



