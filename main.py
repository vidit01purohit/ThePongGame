from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("The Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.update()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

mov_speed = 0.1
game_is_on = True
while game_is_on:
    time.sleep(mov_speed)
    screen.update()
    ball.move()

    # collision with the wall
    if (ball.ycor() > 280 or ball.ycor() < -280):
        ball.bounce_y()

    # collision with right paddle and left paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        mov_speed *= 0.9

    # ball miss the paddle
    if ball.xcor() > 380:
        score.update_l_score()
        ball.reset_position()
        mov_speed = 0.1

    if ball.xcor() < -380:
        score.update_r_score()
        ball.reset_position()
        mov_speed = 0.1

screen.exitonclick()
