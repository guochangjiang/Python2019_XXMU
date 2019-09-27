# 4.3PM2.5Warning
PM = eval(input("请输入PM2.5数值："))
if 0 <= PM < 35:
    print("空气质量优，建议户外活动。")
elif 35 <= PM < 75:
    print("空气质量良，适度户外活动。")
else:
    print("空气污染，出门时请佩戴口罩。")