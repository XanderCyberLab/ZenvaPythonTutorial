from turtle import *

diameter = 40
pop_diameter = 100

bgcolor("black")


def draw_balloon():
    color("red")
    dot(diameter)#draws the balloon by diameter not radius.

def inflate_balloon():
    global diameter #global variable
    diameter = diameter + 20
    draw_balloon()

draw_balloon()
inflate_balloon()

done()




