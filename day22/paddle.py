from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.setpos(position, 0)
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()

    def up(self):
        self.goto(self.position, self.ycor()+20)

    def down(self):
        self.goto(self.position, self.ycor()-20)
