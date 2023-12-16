import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        reduce_car = random.randint(1, 6)
        if reduce_car == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.goto(320, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def game_over(self):
        game_over_text = Turtle()
        game_over_text.write("Game Over", False, "center", ("Courier", 24, "normal"))

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        # print(self.car_speed)