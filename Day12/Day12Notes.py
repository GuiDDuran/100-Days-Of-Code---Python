ENEMIES = 1  # It's called global variable an's in a global scope, and can be used anywhere in the code. Normally,
# we don't change the values of those variables and as a convention, it's declared uppercase.

def increase_enemies():
    enemies = 2  # It's called local variable an's in a local scope, only that function can use this variable.
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {ENEMIES}")


# There is no block scope
game_level = 3
def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]
    print(new_enemy)

create_enemy()
#print(new_enemy)  # This does not work because the variable was crated in a block scope