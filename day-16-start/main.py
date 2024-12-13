# import another_module

# print(another_module.another_variable)

# from turtle import Turtle, Screen

# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)

# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table=PrettyTable()
print(table)


table.add_column("Pokemon",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

table.align="l"
print(table)