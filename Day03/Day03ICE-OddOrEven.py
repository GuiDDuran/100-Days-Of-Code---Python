number = int(input("Write any number to know if it's an even or odd number: "))

if number % 2 == 0:  # If the number can be divided by 2 with 0 remainder.
    print("This is an even number.")
else:  # Otherwise (number cannot be divided by 2 with 0 remainder).
    print("This is an odd number.")
