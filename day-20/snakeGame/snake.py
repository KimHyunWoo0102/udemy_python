from turtle import *


class Snake():
    __starting_positions = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]
    height = 600
    width = 600
    MOVE_DISTANCE=20
    UP=90
    DOWN=270
    RIGHT=0
    LEFT=180

    def __init__(self):
        self.__segment=[]
        self.make_snake()

    def get_head(self):
        return self.__segment[0]

    def make_snake(self):
        """make snake"""
        for position in self.__starting_positions:
            self.add_segment(position)

    def move(self):
        """move forward"""
        head = self.__segment[0]

        prev = head.pos()
        head.forward(self.MOVE_DISTANCE)

        for i in range(1, len(self.__segment)):
            tmp = self.__segment[i].pos()
            self.__segment[i].goto(prev[0], prev[1])
            prev = tmp

    def move_right(self):
        if self.__segment[0].heading() != self.LEFT:
            self.__segment[0].setheading(self.RIGHT)

    def move_left(self):
        if self.__segment[0].heading() != self.RIGHT:
            self.__segment[0].setheading(self.LEFT)

    def move_up(self):
        if self.__segment[0].heading() != self.DOWN:
            self.__segment[0].setheading(self.UP)

    def move_down(self):
        if self.__segment[0].heading() != self.UP:
            self.__segment[0].setheading(self.DOWN)

    def check(self):
        """check if it reachs the boundary of the screen"""
        for item in self.__segment:
            tmp = item.pos()

            if (tmp[0] <= -(self.width/2) or tmp[0] >= self.width/2) or (tmp[1] <= -self.height/2 or tmp[1] >= self.height/2):
                return False

        return True

    def add_segment(self,position):
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.__segment.append(new_segment)

    def extend(self):
        self.add_segment(self.__segment[-1].position())

    def is_touch_body(self):
        for segment in self.__segment[1:]:
            if segment.distance(self.__segment[0])<10:
                return True
        return False