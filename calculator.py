import tkinter
from tkinter import messagebox

root=tkinter.Tk()
root.title("Calculator")

dis=tkinter.Entry(root,width=35,borderwidth=5)
dis.grid(row=0,column=0,columnspan=3)
def button_click(number):
    current=dis.get()
    dis.delete(0, tkinter.END)
    dis.insert(0,str(current)+str(number))
def button_Clear():
    dis.delete(0,tkinter.END)
def button_addition():
    first_num=dis.get()
    global A_num
    global choice
    choice="addition"
    A_num=int(first_num)
    dis.delete(0,tkinter.END)
def button_substract():
    first_num=dis.get()
    global A_num
    global choice
    choice="substract"
    A_num=int(first_num)
    dis.delete(0,tkinter.END)
def button_multiply():
    first_num=dis.get()
    global A_num
    global choice
    choice="multiply"
    A_num=int(first_num)
    dis.delete(0,tkinter.END)
def button_division():
    first_num=dis.get()
    global A_num
    global choice
    choice="division"
    A_num=int(first_num)
    dis.delete(0,tkinter.END)
def button_Equal():
    sec_num=dis.get()
    dis.delete(0,tkinter.END)
    s_num=int(sec_num)
    if choice=="addition":
        res=int(A_num+s_num)
        dis.insert(0,res)
    if choice=="substract":
        res=int(A_num-s_num)
        dis.insert(0,res)
    if choice=="multiply":
        res=int(A_num*s_num)
        dis.insert(0,res)
    if choice=="division":
        res=int(A_num/s_num)
        dis.insert(0,res)



button_1=tkinter.Button(root,text="1",padx=30,pady=20,command=lambda:button_click(1))
button_2=tkinter.Button(root,text="2",padx=30,pady=20,command=lambda:button_click(2))
button_3=tkinter.Button(root,text="3",padx=30,pady=20,command=lambda:button_click(3))
button_4=tkinter.Button(root,text="4",padx=30,pady=20,command=lambda:button_click(4))
button_5=tkinter.Button(root,text="5",padx=30,pady=20,command=lambda:button_click(5))
button_6=tkinter.Button(root,text="6",padx=30,pady=20,command=lambda:button_click(6))
button_7=tkinter.Button(root,text="7",padx=30,pady=20,command=lambda:button_click(7))
button_8=tkinter.Button(root,text="8",padx=30,pady=20,command=lambda:button_click(8))
button_9=tkinter.Button(root,text="9",padx=30,pady=20,command=lambda:button_click(9))
button_0=tkinter.Button(root,text="0",padx=30,pady=20,command=lambda:button_click(0))
button_add=tkinter.Button(root,text="+",padx=30,pady=20,command=button_addition)
button_equal=tkinter.Button(root,text="=",width=13,padx=30,pady=20,command=button_Equal)
button_clear=tkinter.Button(root,text="del",width=13,padx=30,pady=20,command=button_Clear)
button_sub=tkinter.Button(root,text="-",padx=30,pady=20,command=button_substract)
button_mul=tkinter.Button(root,text="x",padx=30,pady=20,command=button_multiply)
button_div=tkinter.Button(root,text="/",padx=30,pady=20,command=button_division)


button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)
button_add.grid(row=5,column=0)
button_sub.grid(row=6,column=0)
button_mul.grid(row=4,column=1)
button_div.grid(row=4,column=2)
button_equal.grid(row=6,column=1,columnspan=2)
button_clear.grid(row=5,column=1,columnspan=2)




root.mainloop()
