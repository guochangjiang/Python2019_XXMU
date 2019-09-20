#3.3.TextProgressBar.py
import time
scale = 10
#方式1：百分比多行非刷新显示
print("方式1：百分比多行非刷新显示")
print("------执行开始------")
for i in range(scale+1):
    c = (i / scale) * 100
    print("%{:3.0f}".format(c))
    time.sleep(0.1)
print("------执行结束------")

#方式2：百分比单行动态刷新显示
print("方式2：百分比单行动态刷新显示")
print("------执行开始------")
for i in range(scale+1):
    c = (i / scale) * 100
    print("\r%{:3.0f}".format(c), end='')
    time.sleep(0.1)
print()
print("------执行结束------")

#方式3：百分比进度条多行非刷新显示
print("方式3：百分比进度条多行非刷新显示")
print("------执行开始------")
for i in range(scale+1):
    a, b = "**" * i, '..' * (scale - i)
    c = (i / scale) * 100
    print("%{:3.0f} [{}->{}]".format(c, a, b))
    time.sleep(0.1)
print("------执行结束------")

#方式4：百分比进度条单行动态刷新显示
print("方式4：百分比单行动态刷新显示")
print("------执行开始------")
for i in range(scale+1):
    a, b = "**" * i, '..' * (scale - i)
    c = (i / scale) * 100
    print("\r%{:3.0f} [{}->{}]".format(c, a, b), end='')
    time.sleep(0.1)
print()
print("------执行结束------")