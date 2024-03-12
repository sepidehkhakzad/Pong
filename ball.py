
from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self, dir):
        super().__init__()
        self.y_pos = random.randint(-100, 100)
        self.move_speed = 0.1
        self.x_pos = 0
        self.x_move = 10
        self.y_move = 10
        self.dir = dir
        self.create()
        self.get_ball_dir()

    def create(self):

        self.color("white")
        self.shape("circle")
        self.pu()
        self.goto(self.x_pos, self.y_pos)

    def move(self):
        # time.sleep(0.1)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def get_ball_dir(self):
        if self.dir == 1:
            self.setheading(random.randint(60, 120) - 90)

            # self.setheading(0)
        elif self.dir == -1:
            self.setheading(random.randint(150, 210))
            # self.setheading(random.randint(40,140)-90)
            # self.setheading(180)

    def turn_y(self):
        self.y_move *= -1

    def turn_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
