# 6.3CalThreeKingdoms.py
import jieba
excludes = {"将军","却说","荆州","二人","不可","不能","如此"}
txt = open("threekingdoms.txt", "r", encoding='utf-8').read()
words  = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word in("孔明", "孔明曰"):
        rword = "诸葛亮"
    elif word in ("关公", "云长", "云长曰"):
        rword = "关羽"
    elif word in ("翼德", "翼德曰"):
        rword = "张飞"
    elif word in ("玄德","玄德曰"):
        rword = "刘备"
    elif word in ("孟德", "丞相", "孟德曰"):
        rword = "曹操"
    else:
        rword = word
    if rword not in excludes:
        counts[rword] = counts.get(rword,0) + 1
top_counts = sorted(list(counts.values()), reverse=True)[:5] # 按值倒序排序，取前10
for count in top_counts:
    for key in counts:
        if counts[key] == count:
            print ("{0:<10}{1:>5}".format(key, count))
