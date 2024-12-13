import sys
from contextlib import nullcontext
from random import random
from turtle import *

turtle_colours = ['red', 'orange', 'yellow', 'green', 'blue','purple']


screen = Screen()
screen.setup(width=500,height=400)
my_turtle = screen.textinput(title="어떤 거북이를 선택할래?", prompt="당신이 원하는 거북이를 선택해주세요!")

def move_random(turtle):
    turtle.forward(int(random()*25+5))

nx=-230
ny=-150

winner=None

if my_turtle in turtle_colours:
    turtles = dict()

    for turtle_color in turtle_colours:
        tmp = Turtle("turtle")
        tmp.color(turtle_color)
        turtles[turtle_color] = tmp

        tmp.penup()
        tmp.goto(x=nx,y=ny)
        ny+=60

    isRun=True

    while isRun:
        for key,turtle in turtles.items():
            move_random(turtle)

            turtle_x=turtle.xcor()

            if turtle_x>230 and not winner:
                winner=key
                isRun=False

    if winner==my_turtle:
        print("축하드립니다! 당신의 거북이가 이겼어요!")
    else :
        print("아깝네요! 다음에는 꼭 이겨봐요!")
    screen.exitonclick()
else:
    print("제대로 입력해 이새끼야")

