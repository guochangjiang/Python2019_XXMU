import tkinter as tk
def myaction():
    S1.set('按钮被点击过了')
top=tk.Tk()
top.geometry('100x100')
S1=tk.StringVar()
top.title='添加按钮'
bn=tk.Button(top,textvariable=S1, command=myaction)
S1.set('按钮1')
bn.pack()
top.mainloop()