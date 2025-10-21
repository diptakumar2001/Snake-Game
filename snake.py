
from turtle import Turtle

START = [(0,0), (-20,0), (-40,0)]
STEP = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0

class Snake:
    def __init__(self):
        self.segments = []
        self.make_snake()

    def make_snake(self):
        for pos in START:
            self._add(pos)

    def _add(self, pos):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(pos)
        self.segments.append(t)

    def extend(self):
        # extend snake body, when collide with food
        self._add(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x, y)
        self.segments[0].forward(STEP)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
