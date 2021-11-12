from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.setposition(0, -240)
        self.movespeed = 0.1

    # For movement of ball all time
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # For bouncing off the upper wall
    def bounce_walls_up(self):
        self.y_move *= -1

    # For bouncing off both the side walls
    def bounce_walls_side(self):
        self.x_move *= -1

    def bounce_paddles(self):
        self.y_move *= -1
        self.movespeed *= 0.9

    # For restarting the ball from original position
    def resetpos(self):
        self.goto(0, -240)
        self.movespeed = 0.1
        self.bounce_paddles()
