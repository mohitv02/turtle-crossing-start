from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.point = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 200)
        self.points()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def points(self):
        self.point = self.point + 1
        self.clear()
        self.goto(0, 270)
        self.write(f"LEVEL{ self.point}", align="center", font=FONT)
