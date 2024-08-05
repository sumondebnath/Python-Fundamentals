# from turtle import Turtle
import turtle as t
import random

tur = t.Turtle()

t.colormode(255)

directions = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tur.speed(0)

for _ in range(200):
    tur.circle(100)
    tur.color(random_color())
    tur.setheading(tur.heading() + 2)