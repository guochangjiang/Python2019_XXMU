#!/usr/bin/env python3

"""
1.1 字符串拼接
接受用户输入的2个字符串，将它们组合后输出，如[某人]想去[某地]看看
"""

str1 = input("请输入一个人的名字：")
str2 = input("请输入一个地方名字：")
print("世界那么大，{}想去{}看看。".format(str1, str2))
#print("世界那么大，%s想去%s看看。" % (str1, str2))