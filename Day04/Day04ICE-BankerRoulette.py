import random
names_string = input("Right all the names: ")
names = names_string.split(", ")
num_items = len(names)  # Get the total number of items in list.
random_number = random.randint(0, num_items - 1)  # Generate random numbers between 0 and the last index.
random_name = names[random_number]  # Choose and print a random name.
print(f"{random_name} is going to buy the meal today!")