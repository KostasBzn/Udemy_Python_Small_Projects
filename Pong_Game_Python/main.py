from turtle import Screen,Turtle
from paddles import  Paddle
from ball import Ball
import time

from scoreboard import Score

screen = Screen()
screen.setup(800, 600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, -0))

ball = Ball()

scoreboard = Score()

screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "q")
screen.onkey(paddle_l.down, "a")


game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 or ball.xcor() < -320:
        ball.bounce_x()

    # r paddle
    if ball.xcor() > 400:
        ball.reset_ball()
        scoreboard.l_point()
    # l paddle
    if ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.r_point()


screen.exitonclick()