# 6.2CalHamlet.py
def getText():
    txt = open("hamlet.txt", "r").read()    # 读取小说内容
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")   #将文本中特殊字符替换为空格
    return txt

excludes = {"the", "and", "of", "you", "a", "i", "my", "in", "to", "well",
           "this", "it", "that", "is", "not", "his", "but", "with", "was",
           "for", "your", "me", "be", "as", "he", "what", "him", "at", "them",
           "so", "have", "will", "do", "on", "all", "our", "by", "like",
           "or", "no", "we", "are", "if", "good", "come", "shall", "sir",
           "o", "thou", "they", "now", "more", "let", "from", "her", "how"}
hamletTxt = getText()
words  = hamletTxt.split()
counts = {}
for word in words:
    if word not in excludes:
        counts[word] = counts.get(word,0) + 1   # word存在时取其次数，否则创建并且次数设为0
top_counts = sorted(list(counts.values()), reverse=True)[:10] # 按值倒序排序，取前10
for count in top_counts:
    for key in counts:
        if counts[key] == count:
            print ("{0:<10}{1:>5}".format(key, count))