from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.color("DodgerBlue")
        self.setposition(x, y)
        self.turtlesize(1, 6)

    def go_left(self):
        new_x = self.xcor() - 25
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 25
        self.goto(new_x, self.ycor())