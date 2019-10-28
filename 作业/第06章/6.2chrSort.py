# 6.2chrSort.py

'''
文本字符分析
编程程序接受字符串，按字符出现频率的降序打印字母。
'''

txt=input("请输入一段英文文本：")
counts={}
for i in txt:
    counts[i]=counts.get(i,0) + 1
items=list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
print("字符按出现频率降序排列为：")
print(''.join([x[0] for x in items]))
print("各字符的出现频率分别为：")
for i in range(len(items)):
    word,count=items[i]
    print("{}：{}；".format(word,count), end='')