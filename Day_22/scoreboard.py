from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.position = position
        self.color("white")
        self.penup()
        self.goto(self.position)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"{self.score}", align="center", font=("arial", 50, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align="center", font=("arial", 50, "normal"))

