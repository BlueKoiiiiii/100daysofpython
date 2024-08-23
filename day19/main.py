import turtle
from turtle import Turtle, Screen
import random
race_on = False
colors = ["red", "orange", "brown", "green", "blue", "purple"]
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race?")
turtle.colormode(255)
all_turtles = []

for i in range(len(colors)):
    tim = Turtle("turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(-230, -150 + i*50)
    all_turtles.append(tim)

if user_bet:
    race_on = True

while race_on:
    for i in range(len(all_turtles)):
        all_turtles[i].forward(random.randint(1, 10))
        if all_turtles[i].xcor()>230:
            winner = all_turtles[i]
            race_on = False

if winner.color() == user_bet.lower():
    print("You were right!")
else:
    print(f"You were wrong! The winner is {winner.color()}")

screen.exitonclick()