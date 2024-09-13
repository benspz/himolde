from turtle import *

def left_ball(n, length):
    angle = 360 / n
    for i in range(n):
        forward(length)
        left(angle)

def right_ball(n, length):
    angle = 360 / n
    for i in range(n):
        forward(length)
        right(angle)

def shaft_right(length):
    setpos(20, -45)
    forward(length)

def shaft_tip(n, length, angle):
    for i in range(n):
        forward(length)
        left(angle)

def shaft_left(length):
    forward(length)
    home()

def penis():
    left_ball(100, 5)
    right_ball(100, 5)
    shaft_right(500)
    shaft_tip(9,15, 20)
    shaft_left(500)

penis()
exitonclick()

