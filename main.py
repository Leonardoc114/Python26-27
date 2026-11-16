#main.py

from myfunctions import *

bob.speed(0)

turtle.Screen().bgcolor("Black")

turtle.colormode(255)
#red triangle
jump(0, 0)
c = (255, 0, 0)
polygon(300, 3, c)

#orange triangle
jump(25, 0)
c = (255, 128, 0)
polygon(250, 3, c)

#yellow triangle
jump(50, 0)
c = (255, 255, 0)
polygon(200, 3, c)

#green triangle
jump(75, 0)
c = (0, 255, 0)
polygon(150, 3, c)

#blue triangle
jump(100, 0)
c = (0, 0, 255)
polygon(100, 3, c)

#magenta triangle
jump(125, 0)
c = (255, 0, 255)
polygon(50, 3, c)

jump(-250, -100)
c = (255, 0, 0)
polygon(100, 5, c)

jump(-250, -100)
c = (255, 128, 0)
polygon(80, 5, c)

jump(-250, -100)
c = (255, 255, 0)
polygon(60, 5, c)

jump(-250, -100)
c = (0, 255, 0)
polygon(40, 5, c)

jump(-250, -100)
c = (0, 0, 255)
polygon(20, 5, c)



