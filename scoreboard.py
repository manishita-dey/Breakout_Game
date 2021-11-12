from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.goto(400, 200)
        self.write(self.score, align='left', font=('Arial', 40, 'normal'))

    def point(self):
        self.score +=5
        self.update_scoreboard()
