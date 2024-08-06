from turtle import Turtle, Screen

tur = Turtle()
screen = Screen()

def move_forward():
    tur.forward(20)

def move_backward():
    tur.backward(20)

def turn_right():
    tur.setheading(tur.heading() - 20)

def turn_left():
    tur.setheading(tur.heading() + 20)

def clear():
    tur.clear()
    tur.penup()
    tur.home()
    tur.pendown()


screen.listen()
screen.onkey(key="f", fun=move_forward)
screen.onkey(key="a", fun=move_backward)
screen.onkey(key="r", fun=turn_right)
screen.onkey(key="w", fun=turn_left)
screen.onkey(key="c", fun=clear)

screen.exitonclick()