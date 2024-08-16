import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from middle import Middle_line

R_PADDLE = 350
L_PADDLE = -350
PADDLE_HITBOX = 50

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(R_PADDLE)
l_paddle = Paddle(L_PADDLE)
ball = Ball()
scoreboard = Scoreboard()
middle = Middle_line()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

on = True

while on:
    screen.update()
    time.sleep(2)
    no_score = True
    while no_score:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()

        # Detects collision with paddle
        if ball.xcor() > 320 and ball.distance(r_paddle) < PADDLE_HITBOX or ball.xcor() < -320 and ball.distance(l_paddle) < PADDLE_HITBOX:
            ball.bounce_x()
        # Detects collision with wall
        elif ball.ycor() > 290 or ball.ycor() < -280:
            ball.bounce_y()

        # If right paddle misses
        if ball.xcor() > 360:
            no_score = False
            ball.reset()
            scoreboard.l_point()
            scoreboard.update_score()

        # If left paddle misses
        if ball.xcor() < -360:
            no_score = False
            ball.reset()
            scoreboard.r_point()
            scoreboard.update_score()

screen.exitonclick()
