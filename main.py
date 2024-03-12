import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)

scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on = True
dir = 1

ball = Ball(dir)

while game_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.turn_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.turn_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.turn_x()

    if ball.xcor() > 370:
        ball.move_speed = 0.1
        ball.goto(0, 0)
        ball.turn_x()
        scoreboard.increase_score_l()
    if ball.xcor() < -370:
        ball.move_speed = 0.1
        ball.goto(0, 0)
        ball.turn_x()
        scoreboard.increase_score_r()

screen.exitonclick()
