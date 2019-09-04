#!/usr/bin/env python3
# 1.5RedStar.py

"""
1.5 五角星的绘制
绘制一个红色的五角星。
"""

import turtle

turtle.pencolor("red")
turtle.begin_fill()
count = 1
while count <= 5:
    turtle.forward(200)  # 向前走200
    turtle.right(144)    # 向右转144度
    count += 1
turtle.fillcolor("red")
turtle.end_fill()
turtle.hideturtle()     # 隐藏海龟
turtle.done()
