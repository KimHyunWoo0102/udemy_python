from turtle import *

class Paddle(Turtle):
    UP=30
    DOWN=-30

    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(x,y)

    def go_up(self):
        self.move(self.UP)

    def go_down(self):
        self.move(self.DOWN)

    def move(self,direction):
        self.goto(self.xcor(),self.ycor()+direction)