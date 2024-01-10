print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))
payment = (total_bill * (tip / 100) + total_bill) / num_people
print(f"Each person should pay: ${"%.2f" % round(payment, 2)}")