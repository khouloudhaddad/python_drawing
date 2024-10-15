from turtle import *

speed(0)
bgcolor("skyblue")

penup()
goto(-250, -100)
pendown()

color("black", "gray") # (outline, fill)
begin_fill()

# Chimney
forward(30)
left(88)
forward(300)
right(88)
forward(50)
right(88)
forward(300)

# First triangle
left(88)
forward(40)
left(90)
forward(100)
right(120)
forward(200)      

# second triangle
left(120)
forward(100)
right(120)
forward(200)

# Finishing off      
right(60)
forward(200)
right(90)
forward(487)
right(90)
forward(200)

end_fill()












