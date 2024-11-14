import turtle

# Initialize the turtle screen and speed
turtle.speed(0)
turtle.hideturtle()

def draw_triangle(side_length, angle):
    """
    Draws an isosceles triangle with the given side length and angle.
    The turtle assumes it's at the vertex of the triangle when the function is called.
    """
    turtle.forward(side_length)
    turtle.left(180 - angle)
    turtle.forward(side_length)
    turtle.left(180 - (2 * angle))
    turtle.forward(side_length)
    turtle.left(180 - angle)  # Return to original orientation

def draw_pie(num_triangles, side_length):
    """
    Draws a pie shape made of 'num_triangles' triangles with side length 'side_length'.
    """
    # Calculate the angle for each triangle based on the number of triangles
    triangle_angle = 360 / num_triangles

    for _ in range(num_triangles):
        draw_triangle(side_length, triangle_angle / 2)  # Draw a single triangle
        turtle.left(triangle_angle)  # Rotate the turtle to form the pie shape

# Usage example: Draw a pie with 10 triangles, each triangle side length of 100
draw_pie(10, 100)

# Finish drawing and display the result
turtle.done()
