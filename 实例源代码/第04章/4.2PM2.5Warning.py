# 4.2PM2.5Warning
PM = eval(input("请输入PM2.5数值："))
if PM >= 75:
    print("空气存在污染，出门时请佩戴口罩。")
else:
    print("空气没有污染，可以户外活动。")

print("空气{}污染！".format("存在" if PM >= 75 else "没有"))