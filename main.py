from turtle import *
from random import *

speed(20)
bgcolor("black")
hideturtle()
width = window_width()
height = window_height()


def draw_star(xpos, ypos):
    star_size = randrange(5, 25)
    penup()
    goto(xpos, ypos)
    pendown()
    dot(star_size, "white")
    

for x in range(100):
    xpos = randrange(-300, width)
    ypos = randrange(-300, height)
    draw_star(xpos, ypos)

done()