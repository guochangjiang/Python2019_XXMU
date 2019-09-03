#!/usr/bin/env python3

"""
1.3 九九乘法表输出
工整打印输出常用的九九乘法表，格式不限。
"""

for i in range(1, 10):
    for j in range(1, i+1):
        print("{}x{}={:2} ".format(j,i,i*j), end='')
    print("")
print("")
# 一行代码
print('\n'.join([' '.join(["%sx%s=%2s" %(j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)]))