from turtle import Turtle, Screen

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def bounce(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def ball_reset(self):
        self.goto(0, 0)
        self.bounce_x()