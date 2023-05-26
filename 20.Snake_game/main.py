from turtle import Screen
import snake
import time
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.title("My Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

food = Food()
snake = snake.Snake()
score_count = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_count.increment_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score_count.final_score()

    for turtles in snake.all_turtles[1:]:
        if snake.head.distance(turtles) < 10:
            game_is_on = False
            score_count.final_score()


screen.exitonclick()
