from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.write(f"LEVEL: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"LEVEL: {self.level}", align="left", font=FONT)

    def end_screen(self):
        self.home()
        self.write("Game Over", align="center", font=FONT)

