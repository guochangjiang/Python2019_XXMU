from datetime import datetime   # 引用datetime库
now = datetime.now()            # 获得当前的日期和时间信息
print(now)
now.strftime("%x")              # 输出其中的日期部分
now.strftime("%X")              # 输出其中的时间部分