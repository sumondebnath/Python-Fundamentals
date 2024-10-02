from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.penup()
        self.goto(0, 320)
        self.color("white")
        self.updatescoreboard()
        self.hideturtle()

    def updatescoreboard(self):
        self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        # self.color("white")
        self.write("Game Over.", align="center", font=("Arial", 24, "normal"))
        # self.hideturtle()

    def increasescore(self):
        self.score += 1
        self.clear()
        self.updatescoreboard()