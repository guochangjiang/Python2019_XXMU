#!/usr/bin/env python3

"""
1.4 计算1!+2!+3!+…+10!
"""


sum = 0
for i in range(1, 11):
    factorial = 1
    for j in range(1, i+1):
        factorial *= j
    sum += factorial

print("1!+2!+3!+…+10!=", sum)
