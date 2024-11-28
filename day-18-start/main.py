#from turtle import *
import turtle as t
import random

timmy_the_turtle=t.Turtle()
colours=["CornflowerBlue","DarkOrchid",'IndianRed','DeepSkyBlue','LightSeaGreen','wheat','SlateGray','SeaGreen']
angles=[0,90,180,270]
speeds=['fastest','fast','normal','slow','slowest']
#timmy_the_turtle.shape("turtle")
#timmy_the_turtle.color("red","green")
#timmy_the_turtle.pencolor("blue")
timmy_the_turtle.width(10)
while True:
    timmy_the_turtle.forward(random.randint(20,100))
    timmy_the_turtle.setheading(random.choice(angles))
    timmy_the_turtle.color(random.choice(colours))
    timmy_the_turtle.speed(random.choice(speeds))


screen=t.Screen()
screen.exitonclick()



