#import colorgram
#
#colors = colorgram.extract('../imgs/image.jpg',30)
#color_dict=[]
#for color in colors:
#    color_dict.append((tuple(color.rgb)))
#
#print(color_dict)

from turtle import *
import random

color_list=[ (213, 222, 215), (223, 211, 215), (209, 156, 94), (172, 86, 46), (220, 206, 114), (140, 147, 27), (221, 75, 126), (108, 181, 219), (213, 119, 155), (43, 124, 79), (161, 54, 97), (17, 125, 186), (143, 35, 18), (89, 28, 82), (69, 149, 132), (216, 83, 49), (16, 102, 30), (104, 35, 86), (132, 173, 151), (229, 206, 19), (225, 171, 188), (175, 205, 178), (9, 79, 20), (110, 25, 7), (221, 178, 166), (64, 145, 181), (191, 191, 193), (158, 202, 215)]

print(len(color_list))
turtle=Turtle()
turtle.penup()
turtle.hideturtle()

colormode(255)
turtle.goto(-200,-200)



for i in range(10):
    turtle.setx(-200)
    turtle.sety(-200+50*i)
    for j in range(10):
        turtle.dot(20,random.choice(color_list))
        turtle.fd(50)

screen=Screen()
screen.exitonclick()