from turtle import Turtle
FONT = ("Arial",40,"normal")
ALIGNMENT = "center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.updateScore()
    def updateScore(self):
        self.clear()
        self.goto(-100,240)
        self.write(f"{self.lscore}",align= ALIGNMENT,font=FONT)
        self.goto(100, 240)
        self.write(f"{self.rscore}", align=ALIGNMENT, font=FONT)
    def lPoint(self):
        self.lscore +=1
        self.updateScore()
    def rPoint(self):
        self.rscore +=1
        self.updateScore()

    def gameOver(self):
        self.goto(0,0)
        self.write("Game Over",align= ALIGNMENT,font=FONT)
