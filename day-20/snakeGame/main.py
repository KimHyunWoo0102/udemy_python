
import time
import random
from turtle import *

from snake import Snake

# dots=[[0]*height]*width




#def make_random_dot():
    #dot=Turtle("circle")
    #dot.color("green")
    #dot.penup()

    #x=int(random.random()*600-300)
    #y=int(random.random()*600-300)

    #dot.goto(x,y)
    #dots[x][y]=dot


screen=Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
#TODO 1: make snake body
snake=Snake()

#TODO 2 : move the snake
screen.listen()
screen.onkey(key="Left",fun=snake.move_left)
screen.onkey(key="Right",fun=snake.move_right)
screen.onkey(key="Up",fun=snake.move_up)
screen.onkey(key="Down",fun=snake.move_down)


while snake.check():
    screen.update()
    time.sleep(0.1)
    snake.move()

    #screen.ontimer(fun=make_random_dot,t=3000)

print("게임 종료!")
screen.exitonclick()

