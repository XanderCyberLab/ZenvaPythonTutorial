from turtle import *
from random import *


bgcolor("black")
hideturtle()
width = window_width()
height = window_height()
speed (0)

def draw_star(xpos, ypos):
    star_size = randrange(5, 25)
    penup()
    goto(xpos, ypos)
    pendown()
    dot(star_size, "white")
    

for x in range(100):
    xpos = randrange(round(-width / 2), round(width))
    ypos = randrange(round(-height / 2), round(height))
    draw_star(xpos, ypos)

done()