#Creating variables
country_name = "United States"
population = 333000000
landlocked = False
border_sqft = 35000000

print(country_name)

#Creating variables for health, damage and potion
hp = 100
damage = 20
potion = 50


hp = hp - damage

print(hp)

hp = hp + potion

print(hp)


#Creating a balloon popper game
#from turtle import *

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

#Attempt to create 3 Balloons. Will need to come back to this.
#from turtle import *

bgcolor("black")

red_balloon_dia = 40
blue_balloon_dia = 60
yellow_balloon_dia = 80

max_diameter = 200

def draw_red_balloon():
    color("red")
    dot(red_balloon_dia)

def draw_yellow_balloon():
    color("yellow")
    dot(yellow_balloon_dia)

def draw_blue_balloon():
    color("blue")
    dot(blue_balloon_dia)
    
draw_red_balloon()
penup()
backward(100)
pendown()
draw_yellow_balloon()
penup()
forward(200)
pendown()
draw_blue_balloon()

def inflate_red_balloon():
    global red_balloon_dia
    red_balloon_dia = red_balloon_dia + 20
    draw_red_balloon()
    
    if red_balloon_dia >= max_diameter:
        clear()
        red_balloon_dia = red_balloon_dia
        write("Pop!")

onkey(inflate_red_balloon, "r")
listen()

done()

#Starry Sky
#from turtle import *
#from random import *


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


#Created a Game Moving the Turtle to the Water
from turtle import *

setup(600, 400)
bgcolor("#C2B280")
move_distance = 50

penup()
color("blue")
goto(100,200)
pendown()


begin_fill()
goto(300, 200)
goto(300, -200)
goto(100, -200)
goto(100, 200)
end_fill()

penup()
goto(-200, 0)

pendown()
shape("turtle")
color("green")

def move_up ():
    setheading(90)
    forward(move_distance)
    check_goal()
    
def move_down ():
    setheading(270)
    forward(move_distance)
    check_goal()

def move_left ():
    setheading(180)
    forward(move_distance)
    check_goal()

def move_right ():
    setheading(0)
    forward(move_distance)
    check_goal()

def check_goal():
    if xcor() > 100: #xcor brings the x position of the turtle
        hideturtle()
        color("white")
        write("You made it to the water!")
        
        onkey(None, "Up")
        onkey(None, "Down")
        onkey(None, "Left")
        onkey(None, "Right")  
               

#Key press events    
onkey(move_up, "Up")
onkey(move_down, "Down")
onkey(move_left, "Left")
onkey(move_right, "Right")
listen()

done()
