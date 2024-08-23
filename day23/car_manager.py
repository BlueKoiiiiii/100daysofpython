COLORS = ["red", "orange", "green", "blue", "purple"]
from turtle import Turtle
import random
import time


class CarManager():
    def __init__(self):
        self.cars = []
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 10

    def generate_new_car(self):
        new_car = Turtle()
        new_car.hideturtle()
        new_car.penup()
        new_car.setheading(180)
        new_car.shape("square")
        new_car.shapesize(1, 3)
        new_car.color(random.choice(COLORS))
        new_car.goto(300, random.randint(-255, 255))
        new_car.showturtle()
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.STARTING_MOVE_DISTANCE)

    def speed_up(self):
        self.STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT
