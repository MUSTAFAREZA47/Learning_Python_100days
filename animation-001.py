import turtle
import random

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
my_turtle = turtle.Turtle()
turtle.colormode(255)
my_turtle.speed("fastest")
my_turtle.width(2)

color_list = [(223, 138, 62), (196, 145, 171), (234, 226, 204), (224, 234, 230), (141, 178, 204), (139, 82, 105),
              (209, 90, 69), (188, 80, 120), (68, 105, 90), (237, 225, 233), (134, 182, 136)]


# Function to draw colorful squares in a spiral
def draw_spiral():
    # colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for _ in range(300):
        my_turtle.color(random.choice(color_list))
        my_turtle.forward(_)
        my_turtle.right(120)
        my_turtle.forward(_)
        my_turtle.right(120)
        my_turtle.forward(_)
        my_turtle.right(120)
        my_turtle.forward(_)
        my_turtle.right(120)
        my_turtle.right(15)


# Hide the turtle for a cleaner look
my_turtle.hideturtle()

# Execute the draw_spiral function
draw_spiral()

# Keep the window open until clicked
turtle.done()
