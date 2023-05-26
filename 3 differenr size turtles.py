import turtle
from itertools import cycle
colors=cycle(['pink', 'maroon', 'yellow', 'light green', 'sky blue', 'purple'])

def draw_circle(size,angle,shit):
    turtle.bgcolor(next(colors))
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shit)
    draw_circle(size+5, angle-20,shit-10)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_circle(30,0,1)
