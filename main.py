from turtle import *

diameter = 40
pop_diameter = 200

bgcolor("black")


def draw_balloon():
    color("red")
    dot(diameter)#draws the balloon by diameter not radius.

def inflate_balloon():
    global diameter #global variable
    diameter = diameter + 20
    draw_balloon()
    
    if diameter >= pop_diameter:
        clear()
        diameter = 40
        write("POP!", font=("Arial", 30, "normal"))
        

draw_balloon()

onkey(inflate_balloon, "Up")
listen()


done()




