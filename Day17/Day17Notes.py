# -- Curiosity --
# PascalCase / camelCase / snake_case
class User:  # The class will contain the attributes and methods related to the user class.
    # pass  # The word pass can be used to 'jump' an empty class or function.

    # The init function is going to be called every time that I create an object from this class.
    def __init__(self, user_id, username):  # The self word is related to the actual object that's being created or initialized.
        print("New user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0  # We can have an attribute that don't need being initialized and can have a default value.
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# Every time this construction happens, the print statement in the init function will be called.
user_1 = User("1", "guilherme")  # Inside the parenthesis I'm passing the attributes that are requires.
print(user_1.id)
print(user_1.username)
print(user_1.followers)

user_2 = User("2", "julia")
print(user_2.id)

# user_2 = User()
# user_2.id = "2"
# user_2.username = "julia"
# print(user_2.username)

user_1.follow(user_2)
print(user_1.following)
print(user_2.followers)

