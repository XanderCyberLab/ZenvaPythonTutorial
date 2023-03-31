from turtle import *

setup(600, 400)
bgcolor("#C2B280")
move_distance = 20

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


done()