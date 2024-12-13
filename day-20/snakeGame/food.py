import random
from turtle import *

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        ranmdom_x = int(random.randint(-280, 280))
        ranmdom_y = int(random.randint(-280, 280))
        self.goto(ranmdom_x, ranmdom_y)
