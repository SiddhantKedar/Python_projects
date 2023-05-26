from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]  # Constants to be written in all CAPS
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]

    def create_snake(self):
        for turtle_index in START_POSITION:
            self.add_segment(turtle_index)

    def add_segment(self, turtle_index):
        the_turtle = Turtle(shape="square")
        the_turtle.color("white")
        the_turtle.penup()
        the_turtle.goto(turtle_index)
        self.all_turtles.append(the_turtle)
        #the_turtle.goto(START_POSITION[turtle_index])

    def extend(self):
        self.add_segment(self.all_turtles[-1].position())

    def move(self):

        for seg_num in range(len(self.all_turtles) - 1, 0, -1):
            x_cord = self.all_turtles[seg_num - 1].xcor()
            y_cord = self.all_turtles[seg_num - 1].ycor()
            self.all_turtles[seg_num].goto(x_cord, y_cord)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
