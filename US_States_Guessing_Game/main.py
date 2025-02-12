import turtle
from turtle import Turtle

import pandas as pd
FONT = ("Courier", 8, "bold")
SCORE_FONT = ("Courier", 24, "bold")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pd.read_csv("./50_states.csv")
states_df = pd.DataFrame(states_data)

score = 0
guessed_states = []

tur = turtle.Turtle()
tur.color("black")
tur.hideturtle()
tur.penup()

scr = turtle.Turtle()
scr.color("black")
scr.hideturtle()
scr.penup()
scr.goto(100, 270)
scr.write(f"Score: {score}/50", font=SCORE_FONT)

def update_score():
    scr.clear()
    scr.write(f"Score: {score}/50", font=SCORE_FONT)

def save_missing_states():
    state_mask = ~states_df["state"].isin(guessed_states)
    missing_states = states_df[state_mask]
    missing_states.to_csv("./not_guessed_states.csv")

game_on = True

while game_on:
    user_input = screen.textinput(title="Guess a state", prompt="State name:").title()
    city_mask = states_df["state"].isin([user_input])
    city_df = states_df[city_mask]

    if user_input == "Exit":
        save_missing_states()
        break

    if not city_df.empty:
        city_name = city_df["state"].item()
        city_x = int(city_df["x"].item())
        city_y = int(city_df["y"].item())
        tur.goto(city_x, city_y)
        tur.write(city_name, font=FONT)
        score += 1
        update_score()
        guessed_states.append(city_name)

    if score == 50:
        print("You won!")
        game_on = False

