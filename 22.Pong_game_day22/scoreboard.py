from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.score_update()

    def score_update(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Ariel", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Ariel", 60, "normal"))

    def l_point(self):
        self.clear()
        self.l_score += 1
        self.score_update()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.score_update()