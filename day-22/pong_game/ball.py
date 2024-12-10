#1. 가운데 생성
#2. 랜덤한 각도와 방향으로 이동
#3. 위 아래 벽 또는 패들에 맞으면

from turtle import *

class Ball(Turtle):
    DX=10
    DY=10

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_speed=0.1

    def move(self):
        self.goto(self.xcor()+self.DX,self.ycor()+self.DY)

    def is_touch_the_wall(self):
        y=self.ycor()
        if y<=-280 or y>=280:
            self.DY=-self.DY

    def x_bounce(self):
        self.DX = -self.DX
        self.move_speed*=0.92

    def is_touch_the_paddle(self,paddle):
        if (self.xcor()>360 or self.xcor()<-360) and self.distance(paddle)<50 :
            self.x_bounce()

    def restart(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.DX*=-1


    def is_over(self):
        if self.xcor()>430:
            self.restart()
            return "right"
        elif self.xcor()<=-430:
            self.restart()
            return "left"
        else:
            return "none"