from turtle import  Turtle
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def grow(self):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(self.snake[-1].xcor(), self.snake[-1].ycor())
        self.snake.append(tim)


    def create_snake(self):
        for i in range(0, 3):
            tim = Turtle(shape="square")
            tim.color("white")
            tim.penup()
            tim.goto(self.x, self.y)
            self.snake.append(tim)
            self.x -= 20

    def move(self):
        for s_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[s_num - 1].xcor()
            new_y = self.snake[s_num - 1].ycor()
            self.snake[s_num].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)