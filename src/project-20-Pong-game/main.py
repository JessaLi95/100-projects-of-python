from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)    # Delete the animation.

paddle_r = Paddle(350, 0)
paddle_l = Paddle(-350, 0)
ball = Ball()
score_board = ScoreBoard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()  # After deleting the animation.
    ball.move()
    screen.listen()
    screen.onkey(paddle_r.up, "Up")
    screen.onkey(paddle_r.down, "Down")
    screen.onkey(paddle_l.up, "w")
    screen.onkey(paddle_l.down, "s")

    # Detect the collision of the top and bottom walls.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # Detect collision with l_paddle
    if ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R Paddle misses
    if ball.xcor() > 380:
        ball.reset_pos()
        score_board.l_add_score()

    # Detect L Paddle misses
    if ball.xcor() < -380:
        ball.reset_pos()
        score_board.r_add_score()

screen.exitonclick()