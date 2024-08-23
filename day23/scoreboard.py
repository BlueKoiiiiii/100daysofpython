FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-270, 250)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over! Your score was {self.level}", align="center", font=("Courier", 24, "normal"))
