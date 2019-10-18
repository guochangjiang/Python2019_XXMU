# 5-1isOdd.py

'''
实现isOdd()函数，参数为整数。
参数如果是奇数，返回真（True），否则返回假（false）。
'''

def isOdd(number):
    if number % 2 != 0:
        return True
    else:
        return False

if __name__ == '__main__':
    number = int(input("请输入一个整数："))
    if isOdd(number):
        print("{}是一个奇数。".format(number))
    else:
        print("{}不是一个奇数。".format(number))