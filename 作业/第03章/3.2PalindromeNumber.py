# 3.2PalindromeNumber.py

'''
如果一个自然数n（如1234321）的各位数字反向排列所得数字与n相等，则n为回文数。
编写程序，从键盘输入一个5位数字，判断该数字是不是回文数。
'''

def isPalindrome(num):
    num_reverse = num[::-1]
    if num == num_reverse:
        return True

num = input("请输入一个自然数N：")
while num.upper() != "N":
    num_isPal = isPalindrome(num)
    if num_isPal:
        print("{}是一个回文数。".format(num))
    else:
        print("{}不是一个回文数。".format(num))
    num = input("请输入一个自然数N：")