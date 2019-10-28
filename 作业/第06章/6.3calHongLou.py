# 6.3calHongLou.py

'''
《红楼梦》人物统计
编程程序统计《红楼梦》中前20位出场最多的人物。
'''
import jieba
excludes = {"什么", "一个", "我们", "如今", "你们", "那里", "说道", "知道", "起来", "这里"}
txt = open("hongloumeng.txt", "r", encoding='utf-8').read()
words  = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word in("宝玉"):
        rword = "贾宝玉"
    elif word in("凤姐", "熙凤"):
        rword = "王熙凤"
    elif word in ("林姑娘", "黛玉"):
        rword = "林黛玉"
    elif word in ("宝钗"):
        rword = "薛宝钗"
    elif word in ("老太太"):
        rword = "贾母"
    else:
        rword = word
    if rword not in excludes:
        counts[rword] = counts.get(rword,0) + 1
top_counts = sorted(list(counts.values()), reverse=True)[:5] # 按值倒序排序，取前10
for count in top_counts:
    for key in counts:
        if counts[key] == count:
            print ("{0:<10}{1:>5}".format(key, count))
