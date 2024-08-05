import turtle as t
import random

tur = t.Turtle()
tur.shape("circle")

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tur.penup()
tur.hideturtle()

tur.setheading(225)
tur.forward(300)
tur.setheading(0)

num_of_dots = 100

for dot in range(1, num_of_dots+1):
    tur.dot(20, random_color())
    tur.forward(50)

    if dot % 10 == 0:
        tur.setheading(90)
        tur.forward(50)
        tur.setheading(180)
        tur.forward(500)
        tur.setheading(0)



screen = t.Screen()
screen.exitonclick()