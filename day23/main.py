import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
timmy = Player()
manager = CarManager()
screen.listen()
scoreboard = Scoreboard()

screen.onkeypress(timmy.move, "Up")
game_is_on = True
time_since_last_car = 0
car_generation_interval = 0.5

while game_is_on:
    if time_since_last_car >= car_generation_interval:
        manager.generate_new_car()
        time_since_last_car = 0
    for car in manager.cars:
        if car.ycor() - timmy.ycor() <= 20 and car.distance(timmy)<= 40:
            game_is_on = False
    if timmy.ycor() >= 250:
        timmy.reset()
        scoreboard.level += 1
        scoreboard.refresh()
        manager.speed_up()
        car_generation_interval -= 0.2
    manager.move_cars()
    time.sleep(0.05)
    time_since_last_car += 0.05
    screen.update()

scoreboard.game_over()

screen.exitonclick()