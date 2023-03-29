from turtle import *

speed (5)
bgcolor("black")

def move_and_turn (distance, angle):
    forward(distance)
    right(angle)
    
color("red")
move_and_turn(100, 45)
move_and_turn(50, 90)
move_and_turn(100, 45)
done()
    



