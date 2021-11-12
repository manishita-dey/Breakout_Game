from turtle import Screen
from bricks import Brick
from ball import Ball
import time
from scoreboard import Scoreboard
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=985, height=600)
screen.title("Breakout Game")
screen.colormode(255)
# animation gets turned off
screen.tracer(0)

# List to hold all the bricks
brick_list = []

# Building the Bricks(Wall)
for x in range(-460,470,65):
    for y in range(-20,150,45):
        brick = Brick(x,y)
        brick_list.append(brick)

# Building the Paddle
paddle = Paddle(0,-270)

# Moving the paddle
screen.listen()
screen.onkeypress(key="Left", fun=paddle.go_left)
screen.onkeypress(key="Right", fun=paddle.go_right)

# Building the Ball
ball = Ball()

# Scoreboard
score = Scoreboard()

# Starting Game
game_is_on = True

# Count for how many times the ball has missed the paddle and restarted
count = 0

while game_is_on:
    screen.update()
    time.sleep(ball.movespeed)
    ball.move()

    #  detect collison with walls:
    # Upper Wall collison
    if ball.ycor() > 280:
        ball.bounce_walls_up()
    # Side Wall Collison
    elif ball.xcor() > 470 or ball.xcor() < - 470:
        ball.bounce_walls_side()


    #     Collison with paddle:
    if ball.ycor() < -240 and ball.distance(paddle) < 50:
        ball.bounce_paddles()

    #     paddle misses
    if ball.ycor() <-310:
        count +=1
        ball.resetpos()


    # Collison with Bricks
    for single_brick in brick_list:
        if ball.distance(single_brick) < 50:
            single_brick.hideturtle()
            brick_list.remove(single_brick)
            ball.bounce_walls_up()
            score.point() #can implement levels by specifying different brick lists and assigning different score to them.


    #Detecting when game is over
    if score.score == 300:
        game_is_on = False
        ball.write('You Win!', align = 'center', font=('Arial', 60, 'normal'))
    elif count == 5:
        game_is_on = False
        ball.write('Game Over', align  = 'center', font=('Arial', 60, 'normal'))






screen.mainloop()