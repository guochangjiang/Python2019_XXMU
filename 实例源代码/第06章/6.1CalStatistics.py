# 6.1CalStatistics

def getNum():   # 获取用户输入
    nums = []
    iNumStr = input("请输入一行数字（逗号隔开）:")
    nums = [eval(i) for i in iNumStr.split(",")]
    return nums

def mean(numbers):  # 计算平均值
    s = 0
    for num in numbers:
        s = s + num
    return s / len(numbers)

def dev(numbers, mean): # 计算标准差
    sdev = 0
    for num in numbers:
        sdev = sdev + (num - mean) ** 2
    return (sdev / (len(numbers) - 1)) ** 0.5

def max_median_min(numbers):
    new = sorted(numbers)
    size = len(numbers)
    mini = new[0]
    maxi = new[-1]
    med = 0
    if size % 2 == 0:
        med = (new[size//2 -1] + new[size//2]) / 2
    else:
        med = new[size//2]
    return (maxi, med, mini)

n = getNum()
m = mean(n)
dev = dev(n, m)
mmm = max_median_min(n)
print("输入的数字为：", n)
print("平均值:{0:.3f}, 标准差:{1:.3f}".format(m, dev))
print("最大值:{0[0]}, 中位数:{0[1]}, 最小值:{0[2]}".format(mmm))