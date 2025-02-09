import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.tracer(0)
screen.listen()

player = Player()
score = Scoreboard()
cars = CarManager()



screen.onkey(player.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    score.update_score()
    cars.create_cars()
    cars.move()

    for car in cars.cars:
        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()


    if player.ycor()== 280:
        score.point()
        cars.speed_increment()
        player.reset_player()
screen.exitonclick()