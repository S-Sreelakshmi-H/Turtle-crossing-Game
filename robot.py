from turtle import Turtle,Screen
sc=Screen()
class Robo(Turtle):
    def __init__(self):
        super().__init__()
        sc.tracer(0)
        self.shape("turtle")

        self.penup()
        self.goto(0,-280)
        self.left(90)
        sc.update()
        # self.showturtle()
    def up(self):
        self.forward(10)
    def refresh(self):
        self.goto(0,-280)
