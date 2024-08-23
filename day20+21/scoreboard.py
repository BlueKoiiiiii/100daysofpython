from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_scores.txt") as file:
            self.high_score = int(file.read())
        self.goto(0, 255)
        self.color("white")
        self.hideturtle()
        self.refresh_score()

    def add_score(self):
        self.score += 1
    def refresh_score(self):
        self.clear()
        self.write(f"Score is: {self.score} High score is: {self.high_score}", align="center", font = ('Arial', 20))



    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_scores.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.refresh_score()
    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(f"Game Over! Your score was {self.score}", align="center", font = ('Arial', 20))