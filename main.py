import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player1 = Player()
screen.listen()

screen.onkey(player1.move_up, "Up")
score = Scoreboard()

game_is_on = True
x = 1
cars = []
while game_is_on:
    time.sleep(0.1)
    if x == 6:
        car = CarManager()
        cars.append(car)
        x = 0

    for car in cars:
        car.move()

    for car in cars:
        if car.distance(player1) < 20:
            game_is_on = False
            score.game_over()

    if player1.ycor() == 260:
        player1.goto(0, -200)
        score.points()
        for car in cars:
            car.reset_motion()

    screen.update()
    x += 1

screen.exitonclick()
