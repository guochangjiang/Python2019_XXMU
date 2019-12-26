import tkinter as tk
def motder(event):
    s='【鼠标事件】\n\n产生事件的控件：{0}\n鼠标位置： (x={1},y={2})'\
       '\n鼠标事件相对屏幕左上角位置：(x={3},y={4})\n'.format(event.widget,
        event.x,event.y,event.x_root,event.y_root,)
    la['text']=s
top=tk.Tk()
top.title='显示鼠标位置'
top.geometry('500x500')
top.resizable(width=False,height=False)
la=tk.Label(top,bg='blue',width=100,height=20,fg='yellow',
            font=('times',14,'bold'))
la.pack()
btn=tk.Button(top,bg='red',text='按钮',width=50,height=20).pack()
top.bind('<Button-1>',motder)
top.mainloop()
