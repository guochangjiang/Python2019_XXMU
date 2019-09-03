#!/usr/bin/env python3

"""
1.5 五角星的绘制
绘制一个红色的五角星。
"""

import turtle

t=turtle.Pen()  #获得画笔
t.hideturtle()  #隐藏海龟
t.pencolor("red")
t.fillcolor("red")
t.begin_fill()
count = 1
while count <= 5:
    t.forward(200)  # 向前走200
    t.right(144)    # 向右转144度
    count += 1
t.end_fill()
ts = turtle.getscreen()
ts.getcanvas().postscript(file="RedStar.eps")
turtle.done()