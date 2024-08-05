from turtle import Turtle
import random

tur = Turtle()

colors = ["cornflower blue", "blue", "light blue", "deep sky blue", "pink", "orange red", "medium slate blue", "dark green"]

def Shape_draw(sides):
    # tur.pensize(5)
    angle = 360 / sides
    for _ in range(sides):
        tur.forward(100)
        tur.right(angle)


for shape_side in range(3, 11):
    # tur.color(random.choice(colors))

    tur.color(colors[shape_side-3])
    Shape_draw(shape_side)