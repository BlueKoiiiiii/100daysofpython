from turtle import Turtle, Screen
import random
import turtle
import colorgram

timmy = Turtle()
turtle.colormode(255)

colorscheme = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

columns = 10
rows = 10
timmy.penup()
timmy.goto(-400, -300)
timmy.speed(0)
timmy.hideturtle()


for j in range(rows):
    for i in range(columns):
        timmy.color(colorscheme[random.randint(0, 4)])
        timmy.dot(50)
        timmy.penup()
        timmy.forward(100)
        timmy.pendown()
    timmy.penup()
    timmy.goto(-400, -300+(j+1)*75)






screen = Screen()
screen.exitonclick()