import turtle
import math

turtle.setup(width=800, height=800, startx=-1, starty=0)

def triangle_90(length) -> None:
    hyp = ((length**2)*2)**0.5
    angle = 135
    turtle.forward(length)
    turtle.left(angle)
    turtle.forward(hyp)
    turtle.left(angle)
    turtle.forward(length)

#triangle_90(50)

def equilateral_triangle(length):
    for _ in range(3):
        turtle.forward(length)
        turtle.left(120)

#equilateral_triangle()

def draw_triangle(radius, angle):
    y = radius * math.sin(angle * math.pi / 180)

    turtle.right(angle)
    turtle.forward(radius)
    turtle.left(90+angle)
    turtle.forward(2*y)
    turtle.left(90+angle)
    turtle.forward(radius)
    turtle.left(180-angle)



def draw_pie(n, radius) -> None:
    angle = 360.0 / n
    for i in range(n):
        draw_triangle(radius,  angle/2)
        turtle.left(angle)

draw_pie(15, 50)


turtle.done()