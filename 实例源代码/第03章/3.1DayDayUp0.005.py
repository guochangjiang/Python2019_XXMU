# 3.1DayDayUp0.005.py

"""
一年365天，每天进步5‰，累计进步多少呢？
一年365天，每天退步5‰ ，累计剩余多少呢？
"""

import math
dayup = math.pow((1.0 + 0.005), 365)
daydown = math.pow((1.0 - 0.005), 365)
print("向上：{:.2f}，向下：{:.2f}.".format(dayup, daydown))