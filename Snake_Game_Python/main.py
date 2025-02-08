from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()

screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
score = Score()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh_food()
        score.score_count()
        snake.grow()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        score.game_over()
        game_on = False

    for s in snake.snake[1:]:
        if snake.head.position() == s.position():
            score.game_over()
            game_on = False








screen.exitonclick()