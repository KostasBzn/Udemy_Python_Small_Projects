from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "bold"))

    def game_over(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER!!", align="center", font=("Arial", 16, "bold"))

    def score_count(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "bold"))


