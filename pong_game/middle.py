from turtle import Turtle

class Middle_line(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, -300)
        self.setheading(90)
        self.pencolor("white")
        self.pensize(2)
        while self.ycor() < 300:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
