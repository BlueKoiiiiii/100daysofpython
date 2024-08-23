from turtle import Turtle, Screen

class snake:
    def __init__(self, length):
        self.segments = []
        for i in range(0, length):
            newsegment = Turtle("square")
            newsegment.color("white")
            newsegment.penup()
            newsegment.goto(0 - i * 50, 0)
            self.segments.append(newsegment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.__init__(3)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].pos())
        self.segments[0].forward(10)
        print(self.segments[0].heading())
    def right(self):
        if self.segments[0].heading() != 180.0:
            self.segments[0].setheading(0)
    def left(self):
        if self.segments[0].heading() != 0.0:
            self.segments[0].setheading(180)
    def up(self):
        if self.segments[0].heading() != 270.0:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() != 90.0:
            self.segments[0].setheading(270)

    def add_segment(self):
        newsegment = Turtle("square")
        newsegment.color("white")
        newsegment.penup()
        newsegment.goto(self.segments[len(self.segments)-1].pos())
        self.segments.append(newsegment)
