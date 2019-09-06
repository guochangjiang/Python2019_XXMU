#2.2DrawPython.v3.py
import turtle
def drawSnake(radius, angle, length):
    turtle.seth(-angle/2)
    for i in range(length):
        turtle.circle(radius, angle)
        #turtle.penup()
        turtle.circle(-radius, angle)
        #turtle.pendown()
    turtle.circle(radius, angle/2)
    turtle.fd(radius)
    turtle.circle(radius*0.4, 180)
    turtle.fd(radius * 2/3)

turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
drawSnake(40, 80, 4)
turtle.done()