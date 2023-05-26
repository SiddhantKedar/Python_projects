from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()

    def increment_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} ", align="center", font=("Ariel", 18, "normal"))

    def final_score(self):
        self.home()
        self.write(f"Game Over", align="center",font=("Ariel",18))
