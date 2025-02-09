from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        if random.randint(1, 7) == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            car.setheading(180)
            car.goto(300, random.randint(-240, 240))
            self.cars.append(car)


    def move(self):
        for car in self.cars:
            car.forward(self.speed)

    def speed_increment(self):
        self.speed += MOVE_INCREMENT

