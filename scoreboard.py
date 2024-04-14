from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-90, 235)
        self.write(f"{self.l_score}", align="center", font=("Helvicta", 120, "normal"))
        self.goto(90, 235)
        self.write(f"{self.r_score}", align="center", font=("Helvicta", 120, "normal"))

    def increase_l_score(self):
        self.l_score += 1
        self.update_score()

    def increase_r_score(self):
        self.r_score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 120, "bold"))
