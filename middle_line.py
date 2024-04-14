from turtle import Turtle


class MiddleLine(Turtle):

    def __init__(self):
        super().__init__()
        self.turt = Turtle(shape="square")

    def create_line(self):
        self.turt.penup()
        self.turt.color("white")
        self.turt.hideturtle()
        self.turt.goto(0, -400)
        self.turt.pensize(5)
        self.turt.shapesize(stretch_len=1, stretch_wid=0.2)
        self.turt.setheading(90)
        for i in range(1, 42):
            if i % 2 == 0:
                self.turt.pendown()
                self.turt.forward(20)
                self.turt.penup()
            else:
                self.turt.forward(20)
