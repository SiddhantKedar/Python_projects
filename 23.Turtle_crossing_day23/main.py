import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()

screen.onkey(player.move, "Up")
scoreboard = Scoreboard()
carmanager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_car()
    carmanager.move()

    for cars in carmanager.all_cars:
        if player.distance(cars) < 20:
            game_is_on = False
            scoreboard.end_screen()

    if player.ycor() > 280:
        player.new_level()
        carmanager.speed_up()
        scoreboard.level_up()

screen.exitonclick()


