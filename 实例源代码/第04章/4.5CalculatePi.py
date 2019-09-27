# 4.5CalculatePi.py
from random import random, uniform
from math import sqrt
from time import time

DARTS = 500000000
hits = 0
start = time()
for i in range(1, DARTS+1):
    x, y = random(), random()
    dist = sqrt(x**2 + y ** 2)
    if dist <= 1.0:
        hits += 1
pi = 4 * (hits / DARTS)
print("Pi值是{}.".format(pi))
print("运行时间是：{:.5f}s".format( time()-start))

hits = 0
start = time()
for i in range(1, DARTS+1):
    x, y = uniform(0.0, 1.0), uniform(0.0, 1.0)
    if x**2 + y ** 2 <= 1.0:
        hits += 1
pi = 4 * (hits / DARTS)
print("Pi值是{}.".format(pi))
print("运行时间是：{:.5f}s".format( time()-start))