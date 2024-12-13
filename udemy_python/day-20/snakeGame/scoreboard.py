from turtle import *

class ScoreBoard(Turtle):
    FONT=("Arial", 12, 'normal')
    ALIGN="center"
    def __init__(self):
        self.score=0
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setposition(0, 280)
        self.write(arg=f"Score: {self.score}", move=False, align=self.ALIGN, font=self.FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=self.ALIGN, font=self.FONT)

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=self.ALIGN,font=self.FONT)

