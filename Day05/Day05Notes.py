fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:  # A basic for statement.
    print(fruit)
    print(fruit + " Pie")
print(fruits)  # It's printed only after the for loop.

# For loop with range
for number in range(1, 6):  # If I want to include the 5, I have to put a bigger number.
    print(number)

print("\n")

for number in range(0, 6, 2):  # By using this last comma, I specify the step.
    print(number)

print("\n")

total = 0
for number in range(1, 101):
    total += number
print(total)