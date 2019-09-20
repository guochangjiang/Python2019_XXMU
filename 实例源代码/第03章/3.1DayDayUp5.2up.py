# 3.1DayDayUp5.2up.py

"""
一年365天，每周末放任，退步1%，一周5个工作日，
每个工作日提高多少，才能达到每天努力1%的效果？
"""

import math
def dayUP(df):
    dayup = 1
    for day in range(365):
        if day % 7 in[0, 6]:
            dayup *= (1- 0.01)
        else:
            dayup *= (1 + df)
    return(dayup)

dayup, dayfactor = 1.0, 0.01
while(dayUP(dayfactor) < 37.78):
    dayfactor += 0.001
print("每天努力的参数是：{:.3f}.".format(dayfactor))