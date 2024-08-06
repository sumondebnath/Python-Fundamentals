from turtle import Turtle, Screen
import random

screen = Screen()

is_race_on = False

screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make Your Guess!", prompt="Enter Your Turtle Color: ")

colors = ["red", "pink", "blue", "purple", "green"]
y_pos = [-100, -50, 0, 50, 100]

all_turtle = []

for tur_idx in range(0, 5):
    tur = Turtle(shape="turtle")
    tur.penup()
    tur.color(colors[tur_idx])
    tur.goto(x=-230, y=y_pos[tur_idx])
    all_turtle.append(tur)


if user_input:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:

        if turtle.xcor() >= 240:
            is_race_on = False

            winner = turtle.pencolor()
            
            if user_input == winner:
                print(f"You Win, the winning color is {winner}!")
            else:
                print(f"You Win, the winning color is {winner}!")

        turtle.forward(random.randint(0, 5))


screen.exitonclick()