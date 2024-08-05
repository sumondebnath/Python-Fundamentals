# from turtle import *
from turtle import Turtle, Screen

timmy = Turtle()

timmy.shape("turtle")
# timmy.shapesize(2)
for i in range(10):
    timmy.color("green")
    timmy.forward(360)
    timmy.write(f"{i}")
    timmy.right(100)
    timmy.forward(360)
    timmy.write(f"{i+1}")
    timmy.right(100)
    timmy.forward(360)


screen = Screen()
screen.exitonclick()