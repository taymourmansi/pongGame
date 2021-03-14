from turtle import Turtle
from random import randint
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("slowest")
        self.xMove = 10
        self.yMove = 10
        self.moveSpeed = 0.1

    def move(self):
        newX = self.xcor() + self.xMove
        newY = self.ycor() + self.yMove
        self.goto(newX,newY)

    def bounceY(self):
        self.yMove *= -1

    def bounceX(self):
        self.xMove *= -1
        self.moveSpeed *=0.9
    def ballReset(self):
        self.goto(0,0)
        self.moveSpeed = 0.1

