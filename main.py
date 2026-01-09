# from turtle import Turtle,Screen
#
# timmy = Turtle()
# # print(timmy.color('blue'))
# # timmy.shape('turtle')
# # timmy.forward(100)
# # timmy.left(90)
# # timmy.forward(100)
# # timmy.right(90)
# # timmy.forward(100)
# # timmy.width(300)
# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         timmy.color(c)
#         timmy.forward(steps)
#         timmy.right(20)
# My_screen = Screen()
# My_screen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("pokemon", ['pikachu','pichu','semipour'])
table.add_column("type", ['electric','water','fire'])

print(table)