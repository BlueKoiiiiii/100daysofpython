from turtle import Screen, Turtle
import random
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
screen = Screen()
score = ScoreBoard()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
leftpaddle = Paddle(-320)
rightpaddle = Paddle(320)
ball = Ball()
game_is_on = True
screen.tracer(0)

screen.listen()
screen.onkeypress(rightpaddle.up, "Up")
screen.onkeypress(rightpaddle.down, "Down")
screen.onkeypress(leftpaddle.up, "w")
screen.onkeypress(leftpaddle.down, "s")

while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()
    if ball.distance(ball.xcor(), 290) < 5 or ball.distance(ball.xcor(), -290) < 5:
        ball.wallbounce()
    if ball.distance(rightpaddle) < 50 and ball.xcor()>rightpaddle.position-20 or ball.distance(leftpaddle) < 50 and ball.xcor()<leftpaddle.position+20:
        ball.paddlebounce()
        ball.speed += 0.5
    if ball.xcor() > 400:
        ball.reset()
        score.l_score += 1
    if ball.xcor() < -400:
        ball.reset()
        score.r_score += 1
    score.refresh()
screen.exitonclick()







