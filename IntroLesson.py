#from turtle import *


# Creating a Square
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)

done()

# Creating a Circle
#Circle with a 50r(100d)
circle(50)

#Testing different shapes

left(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(50)
circle(50)
forward(50)
right(135)
forward(150)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(45)
forward(150)
left(135)
forward(125)

# Adding Color
color("blue")#add color to line. Color must be before the movement
forward(100)
right(90)
color("#900C3F")
forward(100)
color("yellow")
right(90)
forward(100)
color("green")
right(90)
forward(100)

#Challenge create 3 different color circles
#Created Fill Color Circles

begin_fill()
color("orange")
circle(100)
end_fill()
begin_fill()
color("green")
circle(75)
end_fill()
begin_fill()
color("blue")
circle(50)
end_fill()
begin_fill()
color("red")
circle(25)
end_fill()

bgcolor("black")
begin_fill()
color("red")
left(60)
forward(100)
right(120)
forward(100)
right(120)
forward(100)
end_fill()
right(180)
forward(150)
begin_fill()
color("blue")
forward(100)
left(120)
forward(100)
left(120)
forward(100)
left(120)
forward(100)
end_fill()

#Pen up and Pen Down
bgcolor("black")

begin_fill()
color("red")
left(60)
forward(100)
right(120)
forward(100)
right(120)
forward(100)
end_fill()
right(180)
penup()
forward(150)
pendown()
begin_fill()
color("blue")
forward(100)
left(120)
forward(100)
left(120)
forward(100)
left(120)
forward(100)
end_fill()


#Challenge: Create a Solar Like System with Different Color and Size Planets

speed(10)
bgcolor("black")

color("orange")
begin_fill()
circle(30)
end_fill()

penup()
forward(80)
pendown()

color("red")
begin_fill()
circle(20)
end_fill()

penup()
forward(80)
pendown()

color("green")
begin_fill()
circle(40)
end_fill()

penup()
forward(120)
pendown()

color("blue")
begin_fill()
circle(60)
end_fill()

penup()
forward(140)
pendown()

color("yellow")
begin_fill()
circle(50)
end_fill()