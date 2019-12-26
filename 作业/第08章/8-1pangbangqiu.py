from random import random
def printIntro():
    print("这个程序模拟两个乒乓球选手A和B的竞技比赛")
    print("程序运行需要A和B的能力值（以0到1之间的小数表示）")
def getInputs():
    a = eval(input("请输入选手A的能力值(0-1): "))
    b = eval(input("请输入选手B的能力值(0-1): "))
    n = eval(input("模拟比赛的总局数: "))
    return a, b,n
def flag(a,b):            #判断谁发球
    if a ==0 and b==0:    #如果比分是0，说明是开局，随机抽取一方发球
        while True:       #开始抽签
            fl=random()   #抽取一个随机数
            if fl < 0.5:  #小于0.5，A先发球
                return 'A'
            elif fl>0.5:  #大于0.5，B先发球，否则都不是，则继续再次抽取。
                return 'B'
    elif (0<a<10) or (0<b<10): #如果比分在1-10分，根据规则判定该谁发球
        k=int((a+b)/2)         #分数之和取整数商
        if k%2==0 and servingO == 'A':     #商是偶数且第一局是A发球，则A发球
            return 'A'
        elif k%2==0 and servingO == 'B':     #商是偶数且第一局是B发球，则B发球
            return 'B'
        else:                                   #商是奇数
            if servingO == 'A':               #第一局A发球，则奇数是B发球
                return 'B'
            else:                             #否则第一局B发球，则奇数是A发球
                return 'A'
    elif (a>9 and b>9) and ((a+b)%2==0): #如果比分在大于9分，根据规则,偶数场B发球。
        return 'B'
    elif (a>9 and b>9) and ((a+b)%2==1): #如果比分在大于9分，根据规则判定该谁发球
        return 'A'
def simNGames(n, probA, probB):   #获取比赛结果
    winsA, winsB = 0, 0        #初始分为0
    dc={}                  #定义一个字典存储每场比赛的分数
    for i in range(n):     #使用循环，模拟n次比赛
        scoreA, scoreB = simOneGame(probA, probB) #获取单场比赛结果
        dc[i]=[scoreA, scoreB]     #存储单场比赛结果
        if scoreA > scoreB:        #如果A的分数大于B的，A获得一局胜利，否则B获得一局胜利。
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB, dc    #返回比赛结果。
def gameOver(a,b):            #判断比赛是否结束
    if (a>10 or b>10) and abs(a-b)>=2:  #如果比分任意一方达到11分，而且和对方相差2球，则比赛结束。否则，继续比赛。
        return True
    else:
        return False     
def simOneGame(probA, probB):
    scoreA, scoreB = 0, 0        #每场比赛开始，比分清零重新开始
    global servingO                #声明全局变量
    servingO = flag(0,0)              #存储初始发球人
    while not gameOver(scoreA, scoreB):
        serving = flag(scoreA, scoreB) #发球权判断
        if serving == "A":             #A先发球
            if random() < probA:       #A先发球，B接球，根据能力值判断B能否接到球，接不到A加一分
                scoreA += 1
            else:                      #如果B接到球
                if random() < probB:   #B接到球后，根据能力值判断A能否接到球，接不到B加一分。接到的话，进入循环，再次开始A发球，B接球。
                    scoreB += 1
        else:                          #B先发球
            if random() < probB:       #B先发球，A接球，根据能力值判断A能否接到球，接不到B加一分
                scoreB += 1
            else:                      #如果A接到球
                if random() < probA:   #A接到球后，根据能力值判断B能否接到球，接不到A加一分。接到的话，进入循环，再次开始B发球，A接球。
                    scoreA += 1
    return scoreA, scoreB
def printSummary(winsA, winsB,dc):
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print('以下是每局比赛详细信息')
    for i in range(n):
        print('第{}场比赛结果选手A得分：{}分,   选手B得分:{}分'.format(i+1,list(dc[i])[0],list(dc[i])[1]))
    print('以下是比赛总的信息')
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA, winsA/n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB, winsB/n))
def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB, dc = simNGames(n, probA, probB)
    printSummary(winsA, winsB,dc)
main()
