import turtle
from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_right():
    #tim.setheading(tim.heading()+10)
    tim.right(10)

def turn_left():
    tim.left(10)

screen.listen()
screen.onkeypress(key="w",fun=move_forward)
screen.onkeypress(key="s",fun=move_backward)
screen.onkeypress(key="d",fun=turn_right)
screen.onkeypress(key="a",fun=turn_left)

screen.onkey(key="c",fun=tim.reset)
# 매소드를 매개변수로 넘겨주기 위해서는 이름만

screen.exitonclick()

