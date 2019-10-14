# 4.1GuessNumber.py

'''
4.1 猜数游戏
在程序中预设一个1-100的随机整数，让用户通过键盘输入所猜数，若大于预设数，
显示“遗憾，太大了”； 若小于预设数，显示“遗憾，太小了”，如此循环，直
至猜中该数，显示“预测N次，恭喜你猜中了！”。 要求当用户输入非整数时，
给出“输入内容必须为整数！”的提示，并让用户重新输入。
'''

from random import randint

num = randint(1, 100)
print("#"*40)
print("{:^32s}".format("猜数游戏"))
print("#"*40)
guess = input("请输入一个1~100的整数[输入Q结束]：")
t_num = 0
while guess[0] not in ["Q", "q"]:
    t_num += 1
    try:
        if int(guess) == num:
            print("预测{}次，恭喜你猜中了！".format(t_num))
            break
        elif int(guess) > num:
            print("遗憾，太大了！")
        else:
            print("遗憾，太小了！")
    except ValueError:
        print("输入错误，请输入一个整数！")
    guess = input("请再次输入一个1~100的整数[输入Q结束]：")