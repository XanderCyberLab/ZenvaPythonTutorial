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

def say_hello (name):
    print("Hello " + name)
 
say_hello("Alex")
say_hello("Miriam")
say_hello("Juvia")
 
    
#print("Hello Alex")
#print("Hello Miriam")
#print("Hello Juvia")

