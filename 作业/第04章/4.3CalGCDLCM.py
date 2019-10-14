# 4.3CalGCDLCM.py

'''
4.3 最大公约数和最小公倍数计算
从键盘接受2个整数，编写程序求出
这两个整数的最大公约数和最小公倍数
（提示：最小公倍数等于两数之积除以其最大公约数）。
'''

# 辗转相除法求最大公约数
def gcd_Euclidean(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b

# 普通算法求最大公约数
def gcd_general(a, b):
    if a < b:
        a, b = b, a
    i = b
    while a % i != 0 or b % i != 0:
        i -= 1
    return i

# 积/gcd=最小公倍数
def lcm_division(a, b, gcd):
    return a * b // gcd

# 普通算法求最小公倍数
def lcm_general(a, b):
    if a < b:
        a, b = b, a
    i = a
    while i % a != 0 or i % b != 0:
        i += 1
    return i

try:
    num_1, num_2 = eval(input("请输入2个整数[逗号隔开]："))
    num_1 = abs(int(num_1))
    num_2 = abs(int(num_2))
    gcd = gcd_Euclidean(num_1, num_2)
    lcm = lcm_division(num_1, num_2, gcd)
    print("辗转相除法：")
    print("整数{}和{}的最大公约数为{}，最大公倍数为{}".format(num_1, num_2, gcd, lcm))
    gcd = gcd_general(num_1, num_2)
    lcm = lcm_general(num_1, num_2)
    print("一般方法：")
    print("整数{}和{}的最大公约数为{}，最大公倍数为{}".format(num_1, num_2, gcd, lcm))
except:
    print("输入错误，请输入2个整数[逗号隔开]!")