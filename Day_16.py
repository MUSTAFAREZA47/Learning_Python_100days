# Object Oriented Programming


# Link --> https://docs.python.org/3/library/turtle.html
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# # print(timmy)
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.forward(200)
# my_screen = Screen()
# # print(my_screen.canvheight)
# my_screen.exitonclick()


# Link --> https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu","Squirtle", "Charmander"])
table.add_column("Type", ["Electric","Water", "Fire"])
table.align = "l"
print(table)