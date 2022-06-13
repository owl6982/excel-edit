from tkinter import *
import os
from tkinter import filedialog
import tkinter.messagebox
import openpyxl
from pyecharts import Bar
from PIL import ImageTk, Image

root = Tk()
root.title("适用于多种操作系统的访问日志分析统计软件")

group = LabelFrame(root, text='请选择所需服务',padx=5,pady=5)
group.grid(row=4,column=0,columnspan=2, padx=10,pady=10, sticky=E+W)

v = IntVar()
global syss
syss=0
def r1():
    #print('call r1')
    global syss
    syss=1
def r2():
    #print('call r2')
    global syss
    syss=2


SYSTEMS = [
    ('新增项目',1,r1),
    ('项目覆盖',2,r2)]

for sys,num,r in SYSTEMS:
    Radiobutton(group, text=sys,variable=v, value=num,command = r).grid(sticky=W)
   
    

def callback1():
    
    e1.delete(0, END)
    fileName1=StringVar()
    fileName1= filedialog.askopenfilename(filetypes = [("Execl1",".xls")])
    e1.insert('insert' ,fileName1)
    return fileName1

def callback2():
    
    e2.delete(0, END)
    fileName2=StringVar()
    fileName2= filedialog.askopenfilename(filetypes = [("Execl1",".xls")])
    e2.insert('insert' ,fileName2)
    return fileName2


                    
class APP:
    def __init__(self,master,e1,e2, e3, e4):
        
        frame = Frame(master)
        frame.grid(row=5,column=0,columnspan=2,sticky=N+S)
        self.mater=master
        self.hi_there = Button(frame,text="运                                行",bg='black', fg="green",command=self.click1, padx=200)
        #设置调整尺寸和显示位置，如果括号里没东西就按默认来
        self.hi_there.grid(row=5,column=0, columnspan=2)    #这里就默认位置了
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3
        self.e4 = e4

    def click1(self):
        
        if syss==1:
            #print(1)
            if self.e1.get() == ''or self.e2.get() == '':
                return tkinter.messagebox.showinfo('提示','请指定文件位置')
                #判断是否为空，为空返回提示框
            else:
                import excel_add
                excel_add.read_content(content_file1=self.e1.get(),content_file2=self.e2.get(),content_name1=self.e3.get(),content_name2=self.e4.get())
        elif syss==2:
            #print(1)
            if self.e1.get() == ''or self.e2.get() == '':
                return tkinter.messagebox.showinfo('提示','请指定文件位置')
                #判断是否为空，为空返回提示框
            else:
                import excel_cover
                excel_cover.read_content(content_file1=self.e1.get(),content_file2=self.e2.get(),content_name1=self.e3.get(),content_name2=self.e4.get())

    




menubar = Menu(root)
openVar=IntVar()
saveVar=IntVar()
quitVar=IntVar()

filemenu = Menu(menubar, tearoff=False)

filemenu.add_separator()
filemenu.add_command(label="退出", command=root.quit)
menubar.add_cascade(label="文件", menu=filemenu)



v1 = StringVar()
e1 = Entry(root, textvariable=v1, width=65)
e1.grid(row=0, column=0, sticky=E+W,ipadx=100)

v2 = StringVar()
e2 = Entry(root, textvariable=v2, width=65)
e2.grid(row=1, column=0, sticky=E+W,ipadx=100)

v3 = StringVar()
e3 = Entry(root, textvariable=v3, width=65)
e3.grid(row=2, column=0, sticky=E+W,ipadx=100)

v4 = StringVar()
e4 = Entry(root, textvariable=v4, width=65)
e4.grid(row=3, column=0, sticky=E+W,ipadx=100)

Button(root, text="请选择需进行修改的文件" , command= callback1).grid(row=0, column=1)
Button(root, text="请选择需提取信息的文件" , command= callback2).grid(row=1, column=1)
Label(root, text="作为参考的列的名称" ).grid(row=2, column=1)
Label(root, text="需修改的列的名称" ).grid(row=3, column=1)




app = APP(root,e1,e2,e3,e4)


root.config(menu=menubar)


mainloop()
