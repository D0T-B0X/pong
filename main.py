from turtle import Screen
from paddles import Paddle
from middle_line import MiddleLine
from scoreboard import Scoreboard
from ball import Ball
from time import sleep

screen = Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.tracer(0)
r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
screen.update()

screen.tracer(0)
ball = Ball()
score = Scoreboard()
line = MiddleLine()
line.create_line()
screen.listen()
game_on = True

screen.onkeypress(key="Up", fun=l_paddle.paddle_up)
screen.onkeypress(key="Down", fun=l_paddle.paddle_down)
screen.onkeypress(key="w", fun=r_paddle.paddle_up)
screen.onkeypress(key="s", fun=r_paddle.paddle_down)

while game_on:
    screen.update()
    sleep(0.06)

    if ball.distance(l_paddle.position()) < 25 or ball.distance(r_paddle.position()) < 25:
        ball.bounce_on_paddles()
    elif (ball.distance(l_paddle.position()) < 50 or ball.distance(r_paddle.position()) < 50) and (ball.xcor() < -360 or ball.xcor() > 360):
        ball.bounce_on_paddles()
    elif not -380 < ball.ycor() < 380:
        ball.bounce_on_walls()
    elif ball.xcor() > 400 or ball.xcor() < -400:
        if ball.xcor() > 400:
            score.increase_l_score()
            ball.reset_ball("l")
        elif ball.xcor() < -400:
            score.increase_r_score()
            ball.reset_ball("r")
    elif score.l_score == 10 or score.r_score == 10:
        score.game_over()
        game_on = False

    ball.move()


screen.exitonclick()
