#from turtle import *
import turtle as t
import random

def random_color():
    r=random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return tuple((r,g,b))


t.colormode(255)
timmy_the_turtle=t.Turtle()
#colours=["CornflowerBlue","DarkOrchid",'IndianRed','DeepSkyBlue','LightSeaGreen','wheat','SlateGray','SeaGreen']
angles=[0,90,180,270]
speeds=['fastest','fast','normal','slow','slowest']
#timmy_the_turtle.shape("turtle")
#timmy_the_turtle.color("red","green")
#timmy_the_turtle.pencolor("blue")
timmy_the_turtle.width(10)



while True:
    timmy_the_turtle.forward(random.randint(20,100))
    timmy_the_turtle.setheading(random.choice(angles))
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.speed(random.choice(speeds))
screen=t.Screen()
screen.exitonclick()




