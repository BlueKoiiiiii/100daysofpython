STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.hideturtle()
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.showturtle()

    def move(self):
        self.forward(10)

    def reset(self):
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.showturtle()