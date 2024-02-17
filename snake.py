from turtle import Turtle

# in python constants are named with all capital letters
STARTING_POINTS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        # what will happen when we initialise a new snake object. The following two will be triggered
        self.segments = []  # A new attribute
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POINTS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        """ Just like to initialise it again. """
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()   # remove all the items from that list
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())
        # Add a new segment to the snake


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # 2,1, does not include 0
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
