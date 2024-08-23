import turtle

import pandas
from turtle import Turtle, Screen

screen = Screen()
screen.title("US States Game")
data = pandas.read_csv("50_states.csv")

screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

def check_state(state):
    statelist = data.state.to_list()
    for states in statelist:
        if state.lower() == states.lower():
            return(True)
    return(False)

def write_state(statse):
    coodinate = data[data.state == statse.lower()]
    x = coodinate.x.astype('int')
    y = coodinate.y.astype('int')
    newturtle = Turtle()
    newturtle.hideturtle()
    newturtle.setheading(270)
    newturtle.showturtle()
    newturtle.penup()
    newturtle.goto(int(x), int(y))
    newturtle.hideturtle()
    newturtle.write(statse, align="center", font=('arial', 10))



done = False
score = 0
changedprompt = "Whats a state?"
while not done:
    answer_state = screen.textinput(title = "guess_a_state", prompt=changedprompt)
    if check_state(answer_state):
        write_state(answer_state)
        score += 1
        print(f"Your score is:{score}")
        changedprompt = "Whats another state?"
    else:
        changedprompt = "that's not a state, whats another state?"
    if score >= 50:
        done = True

screen.clear()
turtle.hideturtle()
turtle.write("Congratulations! You got all 50 States!", font=("arial", 25), align = "center")









screen.exitonclick()