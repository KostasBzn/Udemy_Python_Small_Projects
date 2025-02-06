import colorgram
import turtle
import random

# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', 10)

tim = turtle.Turtle()
tim.shape("turtle")
turtle.colormode(255)


rgb_colors = []
for color in colors:
    rgb = color.rgb
    r = rgb.r
    g = rgb.g
    b = rgb.b
    rgb_ = (r, g, b)
    rgb_colors.append(rgb_)

turtle.penup()
tim.penup()
turtle.goto(-300, -300)
tim.goto(-300, -300)
y = -300
for j in range(0, 10):
    turtle.penup()
    turtle.goto(-300, y)
    y += 50
    for i in range(0, 10):
        random_color = random.choice(rgb_colors)
        turtle.dot(20, random_color)
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()





screen = turtle.Screen()
screen.exitonclick()