from turtle import *

speed(0)
bgcolor("skyblue")

# Grass
penup()
goto(-400, -100)
pendown()
color("limegreen")
begin_fill()
for i in range(2):
    forward(800)
    right(90)
    forward(400)
    right(90)
end_fill()

# Left mountain
penup()
goto(-400, -100)
pendown()
color("dimgray")
begin_fill()
for i in range(3):
     forward(300)
     left (120)
end_fill()

# Right mountain
penup()
goto(100, -100)
pendown()
begin_fill()
for i in range(3):
     forward(300)
     left (120)
end_fill()



