from turtle import Turtle,Screen
from robot import Robo
ro=Robo()
sc=Screen()
import random

#import
colors=["violet","blue","green","yellow","orange","red"]
class Cars:
    def __init__(self):
        self.all_cars=[]
        self.move_dist = 5
        self.move_incr = 10

    def create(self):
        r=random.randint(1,6)
        if r==1:
            car=Turtle("square")
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.penup()
            car.color(random.choice(colors))
            self.y=random.randint(-250,250)
            sc.tracer(0)#to switch off the tracer, since we don't want to see the car going from centre to the edge
            car.goto(380,self.y)
            sc.update()   #we need the car to be present at the edge from the time the game starts.
            self.all_cars.append(car)

    def move(self):
        for it in self.all_cars:
            it.backward(self.move_dist)
    def move_next(self):
        self.move_dist+=self.move_incr

