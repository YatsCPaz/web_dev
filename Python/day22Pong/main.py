import time
from turtle import Screen, Turtle
from paddle import Paddle
from pong import Pong
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
pong = Pong()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    pong.move()

    # Detect wall collision
    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.wall_bonce()

    # Detect paddle collision
    if pong.distance(right_paddle) < 50 and pong.xcor() > 320 or pong.distance(left_paddle) < 50 and pong.xcor() < -320:
        pong.bonce_back()

    # Detect paddle collision right
    if pong.xcor() > 380:
        pong.reset_position()
        scoreboard.l_point()

    # Detect paddle collision left
    if pong.xcor() < -380:
        pong.reset_position()
        scoreboard.r_point()

screen.exitonclick()