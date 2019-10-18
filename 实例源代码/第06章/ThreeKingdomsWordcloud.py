# 6.3CalThreeKingdoms.py
import jieba
from wordcloud import WordCloud
from PIL import Image
import numpy as np

txt = open("threekingdoms.txt", "r", encoding='utf-8').read()
words  = jieba.lcut(txt)
new_word = []
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
    new_word.append(rword)
string = ' '.join(new_word)
img = Image.open("关公.png")  #打开图片
img_array = np.array(img)    #将图片装换为数组
stopword=[]            #设置停止词，也就是不想显示的词
wc = WordCloud(
    background_color='white',
    width=1000,
    height=800,
    mask=img_array,
    font_path="C:\Windows\Fonts\FZSTK.TTF",
    stopwords=stopword
)
wc.generate_from_text(string) #绘制图片
wc.to_file('三国演义词云.png')  #保存图片