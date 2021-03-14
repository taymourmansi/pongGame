from turtle import Screen
from paddles import Paddles
from ball import Ball
from scoreboard import Scoreboard
import time
SCREEN_WIDTH=800
SCREEN_HEIGHT=600




screen =  Screen()
screen.bgcolor("black")
screen.setup(SCREEN_WIDTH,SCREEN_HEIGHT)
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()

leftPaddle = Paddles()
leftPaddle.createPaddle((-350,0))
rightPaddle = Paddles()
rightPaddle.createPaddle((350,0))
ball = Ball()

screen.listen()
screen.onkey(rightPaddle.up,"Up")
screen.onkey(rightPaddle.down,"Down")
screen.onkey(leftPaddle.up,"w")
screen.onkey(leftPaddle.down,"s")


gameIsOn = True

while gameIsOn:
    screen.update()
    ball.move()
    time.sleep(ball.moveSpeed)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()
    if ball.xcor() < -380:
        scoreboard.rPoint()
        ball.ballReset()
        time.sleep(1)
        ball.bounceX()
    elif ball.xcor() > 380:
        scoreboard.lPoint()
        ball.ballReset()
        time.sleep(1)
        ball.bounceX()

    if ball.distance(leftPaddle) < 50 and ball.xcor() < -320 or ball.distance(rightPaddle) < 50 and ball.xcor() > 320:
        ball.bounceX()


screen.exitonclick()