age = input("Insert your age: ")
years = 90 - int(age)  # At first, we convert the age from string to int, and then we find the number of years left
weeks = years * 52
print(f"You have {weeks} weeks left.")  # After finding the number of weeks left we use the f-string
