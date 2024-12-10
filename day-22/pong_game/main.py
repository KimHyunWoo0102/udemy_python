# TODO 1 : 시작시 공 무작위 생성
# TODO 2 : 막대기에 닿거나 밑/위 바닥에 닿으면 들어온 각도 그대로 뒤집혀서 움직임
# TODO 3 : 양 옆 바닥에 닿으면 공을 사라지게 하고 일정 시간? 뒤에 다시 생성
# TODO 4 : 막대기는 일정한 시간으로 위아래 움직이게 하고 한개는 마우스 or 키보드로 조절가능하게

# class 구분
# 1. 점수판
## 점수에 대한 모든것을 관장
## 처음에는 0 0 하다가 한쪽으로 공이 넘어가면 숫자 올리기
## 이때 두개 만들어서 호출만 다르게
# 2. 공
## 벽에 닿을시 튕기는 기능
## 벽을 넘어가면 increase score 호출
# 3. 막대
## -> 일정한 간격으로 위아래 움직이는 기능 + 입력에 따라 움직이는 기능
## 위 기능은 기본적으로 구현한 막대를 만들고 상속을 해서 오버라이딩하던 하는게 더 좋아보임?

from turtle import *
from score_board import *
from paddle import *
from ball import *
import time

width=800
height=600

screen=Screen()
screen.title('pong')
screen.setup(width,height)
screen.bgcolor("black")
screen.tracer(0)

screen.listen()

tim=Turtle()
tim.hideturtle()
tim.color("white")
tim.penup()
tim.goto(x=0,y=height/2)
tim.setheading(270)

for step in range(0, height, 20):  # 높이에 따라 점선을 그림
    tim.penup()
    tim.forward(10)  # 빈 간격
    tim.pendown()
    tim.forward(10)

score_board1=ScoreBoard(x=-30,y=230)
score_board2=ScoreBoard(x=30,y=230)


my_paddle=Paddle(x=-380,y=0)
com_paddle=Paddle(x=380,y=0)


screen.onkey(key="w",fun=my_paddle.go_up)
screen.onkey(key="s",fun=my_paddle.go_down)
screen.onkey(key='Up',fun=com_paddle.go_up)
screen.onkey(key='Down',fun=com_paddle.go_down)
game_is_on=True

ball=Ball()


while game_is_on:
    screen.update()
    ball.is_touch_the_wall()
    ball.is_touch_the_paddle(my_paddle)
    ball.is_touch_the_paddle(com_paddle)
    ball.move()

    if ball.is_over()=='right':
        score_board1.increase_score()
    elif ball.is_over()=='left':
        score_board2.increase_score()
    time.sleep(ball.move_speed)



screen.exitonclick()