class Mydog:
    '这是一个类'
    color='white'
    def __init__(self,name='jas',master='小明',breed='土狗'):
        self.name=name
        self.master=master
        self.breed=breed
    def wangwang(self):
        print('{}的{}{}狗是{},在汪汪叫'.format(self.master,self.color,self.breed,self.name))
    def doginput(self):
        a=input('请说出您想对小狗说的话:   ')
        fs=open('8-2dog.txt','at')
        fs.write(a)
        fs.close()
def main():
    dog1=Mydog()
    dog2=Mydog('kin','小刘','哈士奇')
    dog1.wangwang()
    dog2.wangwang()
    dog2.doginput()
main()
