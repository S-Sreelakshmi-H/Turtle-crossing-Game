from turtle import Turtle
class Scoreb(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-340,240)
        self.level=1
        self.write(f"Level: {self.level}",False,"center",("Calibri",24,"normal"))
    def inc_level(self):
        self.level+=1
        self.clear()
        self.color("blue")
        self.write(f"Level: {self.level}", False, "center", ("Calibri", 24, "normal"))
    def over(self):
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(0,0)
        self.write("Game over",False,"center",("Arial",48,"bold"))
        self.levels=self.level-1
        if self.level!=1:

            self.goto(0,-30)
            self.write(f"Congratulations for completing level {self.levels}.",False,"center",("Calibri",18,"bold"))