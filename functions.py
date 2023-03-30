def say_hello (name):
    print("Hello " + name)
 
say_hello("Alex")
say_hello("Miriam")
say_hello("Juvia")
 
    
#print("Hello Alex")
#print("Hello Miriam")
#print("Hello Juvia")

def add_and_print(a, b):
    sum = a + b
    print (sum)

def add_numbers (a, b):
    sum = a + b
    return sum
num = add_numbers(100, 50)

print (num)


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
