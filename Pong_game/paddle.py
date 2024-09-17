from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self, cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        # self.goto(350, 0)
        self.goto(cor)

    def go_up(self):
        y_cor = self.ycor()+20
        self.goto(self.xcor(), y_cor)

    def go_down(self):
        y_cor = self.ycor()-20
        self.goto(self.xcor(), y_cor)