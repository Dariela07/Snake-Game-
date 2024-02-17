from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        # shape is the method that Turtle class has
        self.shape('circle')   # we are inheriting from the turtle super class
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randint(-250, 250)  # -300, 300
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)
