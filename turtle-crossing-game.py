from turtle import Turtle,Screen
from cars import Cars
from robot import Robo
from scoreboard import Scoreb
s=Scoreb()

import time
r=Robo()
sc=Screen()
sc.setup(800,600)
c1=Cars()
c1.create()
game_on=True
sc.listen()
sc.onkeypress(r.up,"Up")

while game_on:
    time.sleep(0.1) #c1.create is called i.e.,a car will be created every 0.1 s
    sc.update()
    c1.create()
    c1.move()
    for car in c1.all_cars:
        if car.distance(r)<=25:
            s.over()
            game_on=False
    if r.ycor()>280:
        r.refresh()
        c1.move_next()
        s.inc_level()
sc.exitonclick()

