# 3.1EarthMoonWeight.py

'''
3.1 重量计算
月球上物体重量为在地球上的16.5%，假如某人在地球上每年增长0.5kg，
编写程序输出该人未来10年在地球上和月球上的体重情况。
'''

start_weight = 50
moon_rate = 0.165
growth = 0.5
years = 10

for i in range(1, years+1):
    weight_on_earth = start_weight + growth * i
    weight_on_moon = weight_on_earth * moon_rate
    print("第{:02d}年，在地球和月球上的体重分别为：{:.3f}kg、{:.3f}kg"\
        .format(i, weight_on_earth, weight_on_moon))