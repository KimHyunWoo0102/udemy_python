import turtle as t
#from turtle import *
import random

def random_color():
    r=random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return tuple((r,g,b))

t.colormode(255)
tim = t.Turtle()

for i in range(100):
    tim.speed('fastest')
    tim.setheading(360/100*i)
    tim.color(random_color())
    tim.circle(100)

screen=t.Screen()
screen.exitonclick()