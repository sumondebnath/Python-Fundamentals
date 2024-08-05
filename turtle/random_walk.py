from turtle import Turtle
import random

tur = Turtle()



colors = ["cornflower blue", "blue", "light blue", "deep sky blue", "pink", "orange red", "medium slate blue", "dark green"]
directions = [0, 90, 180, 270]

shapes = ["turtle", "circle", "triangle", "square", "classic"]

tur.speed(0)

for _ in range(500):
    tur.shape(random.choice(shapes))
    tur.color(random.choice(colors))
    tur.pensize(5)
    tur.forward(25)
    tur.setheading(random.choice(directions))