import random
from turtle import Turtle

MOVE_DISTANCE = 10


class Pong(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = MOVE_DISTANCE
        self.y_move = MOVE_DISTANCE
        # self.shapesize(stretch_len=1, stretch_wid=1)
        # self.speed("fastest")

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bonce(self):
        self.y_move *= -1

    def bonce_back(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bonce_back()
