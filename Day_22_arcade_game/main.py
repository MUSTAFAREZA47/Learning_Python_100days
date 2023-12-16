from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("My Ping Pong Game")
screen.bgcolor("black")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
right_scoreboard = Scoreboard((50, 220))
left_scoreboard = Scoreboard((-50, 220))

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.speed_move)
    screen.update()
    ball.move()

    # Debouncing ball as if hit the upper and lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right_paddle and right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

#     if ball left ball miss then right will get the point and vice versa
    if ball.xcor() > 400:
        left_scoreboard.increase_score()
        ball.reset_position()
    elif ball.xcor() < -400:
        right_scoreboard.increase_score()
        ball.reset_position()


screen.exitonclick()
