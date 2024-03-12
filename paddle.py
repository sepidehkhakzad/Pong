from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_pos):
        self.x_pos = x_pos
        super().__init__()
        self.speed("fastest")
        self.create()

    def create(self):

        self.color("white")
        self.shape("square")
        self.pu()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.goto(self.x_pos, 0)

    def move(self):
        self.forward(20)

    def up(self):
        if self.ycor() < 230:
            self.setheading(90)
            self.move()

    def down(self):
        if self.ycor() > -230:
            self.setheading(270)
            self.move()
