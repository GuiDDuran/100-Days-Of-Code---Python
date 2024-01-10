# --Data Types--
# String
print("Hello"[0])  # Doing that, we take the letter in the position 0.
print("123" + "456")  # It's treat like a string and not like a number.

# Integer
print(123 + 345)  # Realize that if we don't use the quotes, it'll be interpreted as a number.
print(123456789)
print(123_456_789)  # Use the underscore makes easier to us visualize the number, but to the computer nothing changes.

# Float
print(3.12345)  # The float numbers are the ones that are not integers.

# Boolean
# There are only two types, and in both the first letter is in uppercase.
True
False

# --Now we'll try to concatenate strings and numbers--
num_char = len(input("What is your name? "))
# print("Your name has " + num_char + "characters.") if we try this, we are going to have a TypeError,
# because it's not possible to concatenate strings and numbers.

print(type(num_char))  # Using the type check function, we can see the type of the variable.

new_num_char = str(num_char)  # By doing that, we convert the int variable to a string.
print("Your name has " + new_num_char + " characters.")

# -- Math operations --
a = 6
b = 2

print("Making operations")
print(a + b)
print(a - b)
print(a * b)
print(a / b)  # The division operation always has a float number as result.
print(a ** b)

# The priority in the operations is:
# ()
# **
# * /
# + -

print(3 * 3 + 3 / 3 - 3)  # It's equal to 7.
print(3 * (3 + 3) / 3 - 3)  # It's equal to 3.

# -- Number manipulation and F string --
print("Rounding numbers")
print(round(8 / 3))  # Using the round function it rounds the number.
print(round(2.67356, 2))  # Putting a number after de comma, we indicate the quantity of decimal numbers we want.

score = 0
# Let´s suppose that the user scores.
score += 1  # Here we are incrementing each time the user scores.
print(score)

# Now you can see that only putting the 'f' in the beginning, makes possible the use of different variable types.
height = 1.8
isWinning = True
print(f"Your score is {score}, your height is {height}, and you are winning is {isWinning}")