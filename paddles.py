from turtle import Turtle

PADDLE_WIDTH = 5
PADDLE_LEN = 1
UP = 90
DOWN = 270

class Paddles(Turtle,):
    def __init__(self):
        super().__init__()

    def createPaddle(self,location):
        self.location = location
        self.shape("square")
        self.shapesize(PADDLE_WIDTH,PADDLE_LEN)
        self.goto(self.location)
        self.color("white")
        self.penup()

    def up(self):
        newYcor = self.ycor()+30
        self.goto(self.xcor(),newYcor)
    def down(self):
        newYcor = self.ycor() - 30
        self.goto(self.xcor(),newYcor)