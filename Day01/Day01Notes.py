# Using input to attribute value to a variable.
name = input("What's your name? ")
print("Hello " + name + "!")

# Using the function len to take the length os the word.
# Using the str() to convert the integer to a string to concatenate. 
length = str(len(name))
print("Your name has " + length + " words.")

# let's invert the value of the variables:
a = "Bruno"
b = "Mars"

temp = a
a = b
b = temp

print("a: " + a)
print("b: " + b)


