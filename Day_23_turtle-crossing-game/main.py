import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard((-200, 250))

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    # when turtle cross finish line then return to initial position
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.increase_score()
        car_manager.level_up()

    # if turtle collide with cars then game is over
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            # print("Game Over")
            car_manager.game_over()
            game_is_on = False


screen.exitonclick()
