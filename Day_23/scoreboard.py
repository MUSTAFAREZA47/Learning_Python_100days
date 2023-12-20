from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.position = position
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(self.position)
        self.update_score()

    def update_score(self):
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)

