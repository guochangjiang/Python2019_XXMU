# 5-2multi.py

'''
实现multi()函数，参数个数不限，返回所有参数的乘积。
'''

def multi(*num):
    product = 1
    for n in num:
        product *= n
    return product

if __name__ == '__main__':
    multiplication = multi(1, 3, 5, 7, 9)
    print("所有参数的乘积是：", multiplication)