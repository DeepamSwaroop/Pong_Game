from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

right_paddle=Paddle((350,0)) #position is passed as tuple
left_paddle=Paddle((-350,0))
ball=Ball()
score=Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down,"Down")
screen.onkey(left_paddle.go_up,"w")
screen.onkey(left_paddle.go_down,"x")

game_is_on =True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with the wall
    if ball.ycor() >280 or ball.ycor() <-280:
        #needs to bounce
        ball.bounce_y()

        #detect collision with paddle
    if ball.distance(right_paddle)<50 and ball.xcor()>320 or ball.distance(left_paddle)<50 and ball.xcor()>-320 :
        ball.bounce_x()

        #detect right paddle misses

    if ball.xcor()>380:
        ball.reset_ball()
        score.l_point()

        # detect right paddle misses

    if ball.xcor()<-380:
        ball.reset_ball()
        score.r_point()

screen.exitonclick()