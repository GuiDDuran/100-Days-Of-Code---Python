print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

# It's an if/else condition, if the condition is true, the instructions in the if block are executed, otherwise the else block is executed.
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    # This if/else inside other if/else statement is called 'Nested if/else'.
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:  # It's an elif statement, it makes possible the use of other conditions.
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    photo = input("Do you want a photo taken? Y or N.")
    if photo == "Y":  # It's a multiple if statement, and it's not necessary an else statement.
        bill += 3  # It's a way to increment a number.

    print(f"Your final bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")

# -- Comparison operators --
# >  - Greater than
# <  - Less than
# >=  - Greater than or equal to
# <=  - Less than or equal to
# ==  - Equal to (it checks if the values are equal)
# !=  - Not equal to

# -- Logical operators --
# A and B, all the conditions have to be true to the statement be true
# C or D, only one of the conditions must be true to the statement be false
# Not E, it changes the value of the condition
