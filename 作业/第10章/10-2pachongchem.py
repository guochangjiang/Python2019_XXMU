#e24CrawUnivRanking.py
import requests
from bs4 import BeautifulSoup
allUniv = []
n=0
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""
def fillUnivList(soup):
    data = soup.find_all('tr',{'class':'bgfd'})   #其它地方也有tr标签，为了确定位置正确，属性值也写上。
    for tr in data:
        n=0
        ltd = tr.find_all('td')
        if len(ltd)==0:
            continue
        singleUniv = []
        for td in ltd:
            n=n+1
            if (n == 5) or (n==6):
                if td.contents==[]:    #如果标签为空，说明没有Img选项，说明没有博士点或者重点学科。
                    td.string='无'
                else:
                 td.string='有'
            
            singleUniv.append(td.string)
        allUniv.append(singleUniv)
def printUnivList(num):
    print("{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format("2019排名","2018排名","百分段位","院校排名","博士点","重点学科","总分"))
    for i in range(num):
        u=allUniv[i]    
        print("{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format(u[0],u[1],u[2],u[3],u[4],u[5],u[6]))

       
def main():
    xueke=input('请输入需要排名的学科')
    url = 'http://www.zuihaodaxue.com/BCSR/'+xueke+'2019.html'
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    fillUnivList(soup)
    printUnivList(20)
main()
