# Function that not allows for input
def greet():
    print("Hello guys, how have you been?")
    print("What's up guys :)")
    print("Hi, how are you?")


greet()


# Function that allows for input
def greet_with_name(name):  # The name is the parameter of the function
    print(f"Hello {name}, how have you been?")
    print(f"What's up {name} :)")
    print(f"Hi {name}, how are you?")


greet_with_name("Guilherme")  # The piece of data where Guilherme is, is called argument


# Function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


greet_with("Guilherme", "Brazil")  # The order of the arguments matter
greet_with("Brazil", "Guilherme")
greet_with(name="Julia", location="Rio de Janeiro") # It's a function with keyword arguments, so here the order doesn't matter

