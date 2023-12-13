import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()

tim.shape("turtle")
tim.speed("fastest")
turtle.colormode(255)

# draw square
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# draw a dashed line
# while True:
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# draw a pentagon
# for _ in range(6):
#     tim.forward(100)
#     tim.right(360/5)

# colors = ["forest green", "cyan", "burlywood", "hot pink", "violet", "coral", "dodger blue"]

# draw random shapes
# def shape(num_side):
#     for _ in range(num_side):
#         tim.forward(100)
#         tim.right(360 / num_side)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     shape(shape_side_n)

# Draw random walks
direction = ["left", "right"]
angle = [0, 90, 180, 270]
walking = True


def random_color():
    r = random.choice(range(1, 255))
    g = random.choice(range(1, 255))
    b = random.choice(range(1, 255))
    random_rgb = (r, g, b)
    return random_rgb


for _ in range(500):
    tim.color(random_color())
    tim.pensize(10)
    tim.forward(30)
    tim.right(random.choice(angle))

screen = Screen()
screen.canvheight = 800
screen.exitonclick()
# screen.colormode(255)
