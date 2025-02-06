import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(600, 400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
names = ["tim", "lara", "jim", "gus", "jen", "asia"]
user_bet = screen.textinput("Make your bet", "Which turtle is going to win? Enter the color: ")
y = -170
turtles = []
for i in range(0, len(names)):
    y += 50
    names[i] = Turtle(shape="turtle")
    names[i].color(colors[i])
    names[i].penup()
    names[i].goto(-270, y)
    turtles.append(names[i])
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() < 270:
            random_distance = random.randint(0, 20)
            turtle.forward(random_distance)
        elif turtle.xcor() >= 270:
            print(f"The {turtle.pencolor()} turtle won!")
            is_race_on = False
            if user_bet == turtle.pencolor():
                print("You guess right!")
            else:
                print("You guess wrong")






screen.exitonclick()