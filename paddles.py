from turtle import Turtle, tracer, update


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def paddle_up(self):
        self.sety(self.ycor() + 20)

    def paddle_down(self):
        self.sety(self.ycor() - 20)

