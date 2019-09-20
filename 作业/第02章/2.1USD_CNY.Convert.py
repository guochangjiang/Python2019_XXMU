#2.1USD_CNY.Convert.py

"""
2.1 汇率兑换程序
按照1美元=7人民币的汇率编写美元与人民币双向兑换程序
"""


# 汇率
rate = 7    # 后期可以通过爬虫从网络上获取精确的实时汇率
# 公式
# USD = RMB * rate
# RMB = USD / rate

def moneyConvert(MoneyStr):
    if MoneyStr[-1] in ['U','u']:
        R = eval(MoneyStr[0:-1]) * rate
        print("{}美元可兑换{:.2f}人民币".format(MoneyStr[0:-1], R))
    elif MoneyStr[-1] in ['R','r']:
        U = eval(MoneyStr[0:-1]) / rate
        print("{}人民币可兑换{:.2f}美元".format(MoneyStr[0:-1], U))
    else:
        print("输入格式错误")

MoneyStr = input("请输入带有符号的美元(U)或者人民币(R): ")
while MoneyStr[-1] not in ["N", "n"]:
    moneyConvert(MoneyStr)
    MoneyStr = input("请输入带有符号的美元(U)或者人民币(R): ")