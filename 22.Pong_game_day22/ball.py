from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xvalue = 10
        self.yvalue = 10
        self.ball_speed = 0.1

    def move(self):
        x_cord = self.xcor() + self.xvalue
        y_cord = self.ycor() + self.yvalue
        self.goto(x_cord, y_cord)

    def bounce_y(self):
        self.yvalue *= -1

    def bounce_x(self):
        self.xvalue *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.home()
        self.ball_speed = 0.1

