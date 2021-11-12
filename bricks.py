from turtle import Turtle
import random

class Brick(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.turtlesize(2,3)
        self.penup()
        r = random.randint(20,255)
        g = random.randint(20,255)
        b = random.randint(20,255)
        random_color = (r, g, b)
        self.color(random_color)
        self.setposition(x, y)


