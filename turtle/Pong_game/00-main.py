from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)


right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()




screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

is_on = True
while is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collusions with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collusion with the right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 400:
        scoreboard.left_point()
        ball.ball_reset()
    
    if ball.xcor() < -400:
        scoreboard.right_point()
        ball.ball_reset()




screen.exitonclick()