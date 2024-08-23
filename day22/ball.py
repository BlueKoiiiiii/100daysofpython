from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.directionx = 1
        self.directiony = 1
        self.speed = 1

    def move(self):
        self.goto(self.xcor()+10*self.directionx*self.speed, self.ycor()+10*self.directiony)

    def wallbounce(self):
        self.directiony *= -1

    def paddlebounce(self):
        self.directionx *= -1

    def reset(self):
        self.goto(0, 0)
        self.speed = 1
        self.directionx *= -1