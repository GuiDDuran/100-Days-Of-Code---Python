programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action fo doing something over and over again."
}  # This is how a dictionary is declared "Key": "Value".

# When we want to retrieve item from dictionary, we need to use the "key" that's associated.
print(programming_dictionary["Bug"])

# Adding new item to dictionary.
programming_dictionary["Integer"] = "A piece of data that's declared as a integer."
print(programming_dictionary)

# Create an empty dictionary.
empty_dictionary = {}
empty_list = []

# Wipe an existing dictionary.
programming_dictionary = {}
print(programming_dictionary)

# Edit an item in a dictionary.
programming_dictionary["Bug"] = "A moth in your computer."
programming_dictionary["Function"] = "A piece of code that does a specific thing."
print(programming_dictionary)

# Loop through a dictionary.
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list in dictionary.
travel_log1 = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting a dictionary in dictionary.
travel_log2 = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Spain": {"cities_visited": ["Madrid", "Barcelona", "Seville"], "non_cities_visited": ["Vigo", "Mùrcia", "Bilbao"]},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# Nesting a dictionary in a list.
travel_log3 = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
]
