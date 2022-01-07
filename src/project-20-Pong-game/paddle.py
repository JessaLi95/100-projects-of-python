from turtle import Turtle

WIDTH = 20 // 20
HEIGHT = 100 // 20


class Paddle(Turtle):
    def __init__(self, X, Y):
        super().__init__()
        self.penup()
        self.setpos(X, Y)
        self.color("white")
        self.shape("square")
        self.shapesize(HEIGHT, WIDTH)

    def up(self):
        self.sety(self.ycor() + 20)

    def down(self):
        self.sety(self.ycor() - 20)
