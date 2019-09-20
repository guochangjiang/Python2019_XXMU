# 3.1DayDayUp5.2.py

"""
一年365天，一周5个工作日，每个工作日努力学习，提高1%，
周末放任一下，退步1%，效果如何？
"""

import math
dayup, dayfactor = 1.0, 0.01
for day in range(365):
    if day % 7 in[0, 6]:
        dayup *= (1- dayfactor)
    else:
        dayup *= (1 + dayfactor)
print("向上5天，向下2天的力量：{:.2f}.".format(dayup))