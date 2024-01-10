two_digit_number = input("Please, write a number: ")
first_digit = int(two_digit_number[0])  # At first, we take the digit in position 0, then we convert the string into integer.
second_digit = int(two_digit_number[1])  # At first, we take the digit in position 1, then we convert the string into integer.
two_digit_number = first_digit + second_digit  # Now, with the two digits as an integer, we can make the operation.
print(two_digit_number)
