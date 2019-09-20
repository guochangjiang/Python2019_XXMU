#3.4.TextProgressBar.v2.py
import time
scale = 50
print("{:-^{}}".format("执行开始", scale//2))
t = time.clock()
for i in range(scale+1):
    a = "*" * i
    b = '.' * (scale - i)
    c = (i / scale) * 100
    t  -= time.clock()
    print("\r{:3.0f}%[{}->{}] {:.2f}s".format(c, a, b, abs(t)), end='')
    time.sleep(0.1)
print()
print("{:-^{}}".format("执行结束", scale//2))