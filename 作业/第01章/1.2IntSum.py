#!/usr/bin/env python3

"""
1.2 整数序列求和
用户输入一个正整数N，计算从1到N相加之和。
"""

n = input("输入整数N：")
# 方法1
sum = 0
i = 1
while i <= int(n):
    sum += i    # sum = sum + i + 1
    i += 1      # 一定不要忘记！
print("1到N的和为：", sum)
# 方法2
sum = 0
# range(N)相当于0,1,2,...,N-1
for i in range(int(n)):
    sum += i + 1    # sum = sum + i + 1
print("1到N的和为：", sum)

# 方法3
sum = 0
# range(1, N)相当于1,2,...,N-1
for i in range(1, int(n)+1):
    sum += i    # sum = sum + i
print("1到N的和为：", sum)