from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)


    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        if new_y <= FINISH_LINE_Y:
            self.goto(0, new_y)

    def reset_player(self):
        self.goto(STARTING_POSITION)
