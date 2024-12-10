from turtle import *

class ScoreBoard(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.color("white")
        self.score = 0

        self.hideturtle()
        self.goto(x, y)
        self.update_scoreboard()


    def increase_score(self):
        self.score+=1
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"{self.score}", move=False, align="center", font=("Arial", 50, "normal"))