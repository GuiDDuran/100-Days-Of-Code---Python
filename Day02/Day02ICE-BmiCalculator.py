print("Enter height in meters: ")
height = input()
print("Enter weight in kilograms: ")
weight = input()
height_measure = float(height)  # Convert the string to float.
weight_measure = float(weight)  # Convert the string to float.
bmi = weight_measure / height_measure ** 2  # Make the operation.
bmi_as_int = int(bmi)  # Convert the float result to an integer.
print("Your BMI is " + str(bmi_as_int))