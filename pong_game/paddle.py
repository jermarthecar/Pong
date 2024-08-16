from turtle import Turtle



MOVE = 35
class Paddle(Turtle):


    def __init__(self, xcor):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.shapesize(stretch_wid=0.5, stretch_len=5)
        self.setx(xcor)

    def up(self):
        self.forward(MOVE)

    def down(self):
        self.back(MOVE)
