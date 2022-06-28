from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG !💥")
screen.listen()
screen.tracer(0)


paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.onkeypress(paddle1.move_up, "Up")
screen.onkeypress(paddle1.move_down, "Down")
screen.onkeypress(paddle2.move_up, "w")
screen.onkeypress(paddle2.move_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # collison with wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect paddle collision
    if (ball.distance(paddle1) < 50 and ball.xcor() > 320):
        ball.bounce_x_r_paddle()
    if (ball.distance(paddle2) < 50 and ball.xcor() < -320):
        ball.bounce_x_l_paddle()

    # detect paddle collision
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # left paddle collision
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
