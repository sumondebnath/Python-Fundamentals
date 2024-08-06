from turtle import Turtle, Screen

tur = Turtle()
screen = Screen()

def move():
    tur.forward(20)


screen.listen()
screen.onkey(key="space", fun=move)

screen.exitonclick()