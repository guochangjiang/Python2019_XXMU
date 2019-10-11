import datetime
import turtle
def drawGap(): #绘制数码管间隔
    turtle.penup()
    turtle.fd(5)
def drawLine(draw): #绘制单端数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
def drawDigit(d): #根据数字绘制七段数码管
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)  #第1个数码管段
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)  #第2个数码管段
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)   #第3个数码管段
    drawLine(True) if d in [0,2,6,8] else drawLine(False) #第4个数码管段
    turtle.left(90)  #画笔方向朝上
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False) #第5个数码管段
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False) #第6个数码管段
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False) #第7个数码管段
    turtle.left(180)  # 画笔方向定位右边
    turtle.penup()
    turtle.fd(20)
def drawDate(date): #获得需要输出的数字
    turtle.pencolor('red')
    for i in date:
        if i == '-':
            turtle.write('年',font=('Arial',18,'normal'))
            turtle.pencolor('green')
            turtle.fd(40)
        elif i == '=':
            turtle.write('月',font=('Arial',18,'normal'))
            turtle.pencolor('blue')
            turtle.fd(40)
        elif i == '+':
            turtle.write('日',font=('Arial',18,'normal'))
        else:
            drawDigit(eval(i)) #注意：通过eval()函数将数字变为整数
def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(datetime.datetime.now().strftime('%Y-%m=%d+'))
    turtle.done()
main()


