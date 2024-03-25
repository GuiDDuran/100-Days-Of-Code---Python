target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0:  # Changed the condition
    print("FizzBuzz")
  elif number % 3 == 0:  # Changed to an elif statment
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)