from turtle import Turtle, Screen

tur = Turtle()

tur.shape("classic")

for _ in range(10):
    tur.pendown()
    if _ % 2 == 0:
        tur.color("pink")
    else:
        tur.color("green")
    tur.forward(20)
    tur.penup()
    tur.forward(25)



screen = Screen()
screen.exitonclick()