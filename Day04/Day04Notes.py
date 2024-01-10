# -- Randomization --
import random  # Here we are importing a library to use the randomization.
import Day04MyModule  # And here I'm importing a module that I created.

random_integer = random.randint(1, 10)  # Using the .randint we can generate a random integer.
print(random_integer)

random_float = random.random()  # Using the .random we can generate a random float between 0.000... to 0.999...
print(random_float)

print(Day04MyModule.pi)  # By doing that I can use a variable declared in another module.

# -- Lists and some functions --

states_of_america = ["Delaware", "Pennsylvania", "California"]  # This is how we create a list.

print(states_of_america[0])  # Doing that we can take the value in the position 0.
print(states_of_america[-1])  # We can also take a negative value, like in the position -1.

states_of_america[1] = "Pencilvania"  # When we do that, we change the value of the variable in the position 1

states_of_america.append("Missouri")  # The append function, add a single item at the end of the list

states_of_america.extend(["Nevada", "Mississippi", "Oregon"])  # The extend function, "add" a list to the end of the current list
# For more list functions, search the documentation on Google

print(states_of_america)

num_of_states = len(states_of_america)  # Using the len function we can see the size of the list
print(num_of_states)

# print(states_of_america[num_of_states]), This sentence will give us this error - IndexError: list index out of range
# because we have to subtract 1 to be on the range of the list

print(states_of_america[num_of_states - 1])

# -- Nested Lists --

fruits = ["Strawberries", "Apples", "Bananas"]
vegetables = ["Tomatoes", "Potatoes", "Spinach"]

dirty_dozen = [fruits, vegetables]  # It's called a nested list
print(dirty_dozen)
print(dirty_dozen[0][1])  #If we do that, we will take the element in the first list [0], and the second element inside this list [1]