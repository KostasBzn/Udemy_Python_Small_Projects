import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("orange")
        self.speed("fastest")
        self.refresh_food()


    def refresh_food(self):
        random_x = random.randint(-250, +250)
        random_y = random.randint(-250, +250)
        self.goto(random_x, random_y)