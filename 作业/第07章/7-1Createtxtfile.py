str1=input('请输入您要写入文件的话：')
fs=open('7-1Createtxtfile.txt','at')
fs.write(str1)
fs.close()