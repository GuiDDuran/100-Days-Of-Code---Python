from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()  # Here we have the Turtle class, represented by an uppercase letter.
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DeepPink")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)  # Here we use an attribute of the Screen class.
# my_screen.exitonclick()  # It's a method of the Screen class.

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
