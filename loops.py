num = 0


for x in range(10):
    num = num + 1
    print(num)
    
    
#from turtle import *

bgcolor("black")

def create_octagon():
    color("red")
    for x in range(8):
        forward(100)
        right(45)

#create_octagon()

def create_shape(angle, sides):
    color("blue")
    for x in range(sides):
        forward(100)
        right(angle)

create_shape(90, 4)    
    
done()