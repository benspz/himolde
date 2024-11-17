import turtle

def draw_triangle(side_length, angle):
    ...

def draw_pie(n, radius):
    corners = []
    for _ in range(n):
        turtle.forward(radius)
        corners.append(turtle.pos())
        turtle.left(180)
        turtle.forward(radius)
        turtle.left(180 - 360/n)
    turtle.setpos(corners[0])
    for i in range(n):
        turtle.goto(corners[i])
    turtle.goto(corners[0])

draw_pie(20, 50)
turtle.done()
