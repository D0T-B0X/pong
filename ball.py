from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0, -379)
        self.setheading(135)

    def bounce_on_paddles(self):
        if 90 < self.heading() < 180:
            angle = self.heading() - 90
            self.setheading(angle)
        elif 180 < self.heading() < 270:
            angle = self.heading() + 90
            self.setheading(angle)
        elif 270 < self.heading() < 360:
            angle = self.heading() - 90
            self.setheading(angle)
        elif 0 < self.heading() < 90:
            self.setheading(2 * self.heading())
        elif self.heading() == 90 or self.heading() == 180 or self.heading() == 270 or self.heading() == 360:
            self.setheading(self.heading() + 45)

    def bounce_on_walls(self):
        if 90 < self.heading() < 180:
            angle = self.heading() + 90
            self.setheading(angle)
        elif 180 < self.heading() < 270:
            angle = self.heading() - 90
            self.setheading(angle)
        elif 270 < self.heading() < 360:
            angle = self.heading() - 270
            self.setheading(angle)
        elif 0 < self.heading() < 90:
            angle = self.heading() + 270
            self.setheading(angle)

    def move(self):
        self.forward(20)

    def reset_ball(self, a):
        self.goto(0, -379)
        if a == "l":
            self.setheading(135)
        elif a == "r":
            self.setheading(45)
