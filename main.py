from turtle import *

setup(600, 400)
bgcolor("#C2B280")
move_distance = 100

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
    
def move_down ():
    setheading(270)
    forward(move_distance)

def move_left ():
    setheading(180)
    forward(move_distance)

def move_right ():
    setheading(0)
    forward(move_distance)
    
onkey(move_up, "Up")
onkey(move_down, "Down")
onkey(move_left, "Left")
onkey(move_right, "Right")
listen()

done()