import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PYPassword Generator!")
number_letters = int(input("How many letters would you like in your password? "))
number_symbols = int(input("How many symbols would you like? "))
number_numbers = int(input("How many numbers would you like? "))

# Easy Level
password = ""
for char in range(1, number_letters + 1):
    password += random.choice(letters)

for char in range(1, number_symbols + 1):
    password += random.choice(symbols)

for char in range(1, number_numbers + 1):
    password += random.choice(numbers)

print(password)

# Hard Level
password_list = []
for char in range(1, number_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, number_symbols + 1):
    password_list.append(random.choice(symbols))

for char in range(1, number_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)  # The shuffle randomize de elements of the list

password = ""

for char in password_list:
    password += char

print(password)