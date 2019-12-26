#e24CrawUnivRanking.py  
import requests
from bs4 import BeautifulSoup
allUniv = []
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""
def fillUnivList(soup,shen):
    data = soup.find_all('tr')
    for tr in data:
        ltd = tr.find_all('td')
        if len(ltd)==0:
            continue
        singleUniv = []
        for td in ltd:
            singleUniv.append(td.string)
        if singleUniv[2]==shen:             #总列表添加相关查询省市的大学信息
            allUniv.append(singleUniv)
def printUnivList(num=0):
    print("{:^4}{:^10}{:^5}{:^8}".format("排名","学校名称","省市","总分"))
    if num==0:
        num=len(allUniv)
    for i in range(num):
        u=allUniv[i]
        print("{:^4}{:^10}{:^5}{:^8}".format(u[0],u[1],u[2],u[3]))
def main():
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    sheng=input('请输入需要排名的省市：  ')
    num=input('请输入需要获取该省排名大学的个数（0代表全部获取）：  ')
    print('\n\n\n')
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    fillUnivList(soup,sheng)
    printUnivList(eval(num))
main()
