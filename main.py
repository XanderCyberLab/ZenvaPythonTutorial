from turtle import *

bgcolor("#C2B280")

move_distance = 20
# Create a screen size 500 x 800 pixels
setup(600, 400)



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

done()