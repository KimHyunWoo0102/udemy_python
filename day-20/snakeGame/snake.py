from turtle import *


class Snake():
    __starting_positions = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]
    height = 600
    width = 600
    MOVE_DISTANCE=20
    UP=90
    DOWN=270
    RIGHT=90
    LEFT=180

    def __init__(self):
        self.__snakes=[]
        self.make_snake()

    def make_snake(self):
        """make snake"""
        for position in self.__starting_positions:
            snake_body = Turtle("square")
            snake_body.penup()
            snake_body.color("white")
            snake_body.goto(position)
            self.__snakes.append(snake_body)

    def move(self):
        """move forward"""
        head = self.__snakes[0]

        prev = head.pos()
        head.forward(self.MOVE_DISTANCE)

        for i in range(1, len(self.__snakes)):
            tmp = self.__snakes[i].pos()
            self.__snakes[i].goto(prev[0], prev[1])
            prev = tmp

    def move_right(self):
        if self.__snakes[0].heading() != self.LEFT:
            self.__snakes[0].setheading(self.RIGHT)

    def move_left(self):
        if self.__snakes[0].heading() != self.RIGHT:
            self.__snakes[0].setheading(self.LEFT)

    def move_up(self):
        if self.__snakes[0].heading() != self.DOWN:
            self.__snakes[0].setheading(self.UP)

    def move_down(self):
        if self.__snakes[0].heading() != self.UP:
            self.__snakes[0].setheading(self.DOWN)

    def check(self):
        """check if it reachs the boundary of the screen"""
        for item in self.__snakes:
            tmp = item.pos()

            if (tmp[0] <= -(self.width/2) or tmp[0] >= self.width/2) or (tmp[1] <= -self.height/2 or tmp[1] >= self.height/2):
                return False

        return True