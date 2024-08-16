from turtle import Turtle
import time

class Ball(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        # self.setheading(random.randint(0,359))
        # self.setheading(10)
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.05

    def move(self):
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.home()
        self.bounce_x()
        self.move_speed = 0.09
