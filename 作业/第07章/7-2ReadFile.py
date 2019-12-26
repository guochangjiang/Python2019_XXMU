str1=input('请输入您要打开的文件：')
fs=open(str1,'rt')
i=0
for line in fs:
    i=i+1
    print('{}行:  {}'.format(i,line))
fs.close()
