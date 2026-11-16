#myfunctions.py
import turtle

bob = turtle.Turtle()
bob.speed(0)


def polygon(dist, sides, c):
    angle = 360/sides
    bob.color(c)
    bob.begin_fill()
    for times in range(sides):
        bob.forward(dist)
        bob.left(angle)
    bob.end_fill()

def jump(x, y):
    bob.penup()
    bob.goto(x, y)
    bob.pendown()
