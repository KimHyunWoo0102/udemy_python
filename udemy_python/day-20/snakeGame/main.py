
import time
from turtle import *

from snake import Snake
from food import Food
from scoreboard import ScoreBoard

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

# TODO 3 : make Food
food=Food()

score_board=ScoreBoard()

isRun=True

while isRun:
    screen.update()
    time.sleep(0.1)
    snake.move()


    isRun = snake.check() and not snake.is_touch_body()

    if food.distance(snake.get_head()) < 15:
        food.refresh()
        score_board.increase_score()
        snake.extend()


score_board.game_over()
screen.exitonclick()

