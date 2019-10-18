# 5-3mysysdatetime

'''
使用datetime库，获取系统时间并按照自己喜欢个一种格式输出。
'''

from datetime import datetime

today = datetime.now()
print(today)
print(today.strftime("%Y-%m-%d %H:%M:%S"))