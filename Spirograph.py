import turtle
from turtle import Turtle, Screen
import random

tinny = Turtle()
turtle.colormode(255)
tinny.speed("fastest")


def random_color():
    r = random.choice(range(1, 255))
    g = random.choice(range(1, 255))
    b = random.choice(range(1, 255))
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    number_turns = int(360 / size_of_gap)
    for _ in range(number_turns):
        tinny.color(random_color())
        tinny.circle(100)
        tinny.setheading(tinny.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.canvheight = 800
screen.exitonclick()
