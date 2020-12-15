from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(f"{COLORS[random.randint(0, 5)]}")
        self.penup()
        self.left(180)
        self.goto(300, random.randint(-250, 250))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 10

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)

    def reset_motion(self):
        self.STARTING_MOVE_DISTANCE = self.STARTING_MOVE_DISTANCE + self.MOVE_INCREMENT
