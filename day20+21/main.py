import time
from turtle import Turtle, Screen
from snack import snake
from food import Food
from scoreboard import ScoreBoard
import random

screen = Screen()
timmy = snake(4)
food = Food()
scoreboard = ScoreBoard()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snack")
screen.tracer(0)
game_is_on = True
screen.listen()

screen.onkey(timmy.up, "w")
screen.onkey(timmy.left, "a")
screen.onkey(timmy.down, "s")
screen.onkey(timmy.right, "d")

while game_is_on:
    time.sleep(0.05)
    screen.update()
    timmy.move()

    if timmy.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.add_score()
        scoreboard.refresh_score()
        timmy.add_segment()

    if timmy.segments[0].xcor() > 280 or timmy.segments[0].xcor() < -280 or timmy.segments[0].ycor() > 280 or timmy.segments[0].ycor() < -280:
        scoreboard.reset()
        timmy.reset()

    for i in timmy.segments[2:len(timmy.segments)]:
            if timmy.segments[0].distance(i) < 5:
                scoreboard.reset()
                timmy.reset()

screen.exitonclick()