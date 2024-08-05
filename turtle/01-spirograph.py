# from turtle import Turtle
import turtle as t
import random

tur = t.Turtle()

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tur.speed(0)

def draw_spirograph(gaps):
    for _ in range(int(360 / gaps)):
        tur.circle(100)
        tur.color(random_color())
        tur.setheading(tur.heading() + gaps)


draw_spirograph(2)

screen = t.Screen()
screen.exitonclick()