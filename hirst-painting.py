# import colorgram
import random
import turtle
from turtle import Turtle, Screen


# colors = colorgram.extract('xyz.jpeg', 15)
# rgb_color = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
#
# print(rgb_color)


tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
turtle.colormode(255)
color_list = [(223, 138, 62), (196, 145, 171), (234, 226, 204), (224, 234, 230), (141, 178, 204), (139, 82, 105),
              (209, 90, 69), (188, 80, 120), (68, 105, 90), (237, 225, 233), (134, 182, 136)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(30, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)






screen = Screen()
screen.canvheight = 800
screen.exitonclick()