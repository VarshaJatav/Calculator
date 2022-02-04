
from tkinter import *

root=Tk()
root.title("Calculator")
root['bg']='black'
e=Entry(root,width=43,bd=10,bg="black",fg="white")
e.grid(row=0,column=0,columnspan=4)
def fun(n):
    num=e.get()
    e.delete(0,END)
    e.insert(0,str(num)+str(n))

def func():
    e.delete(0,END)

global num
global b
def funct(n):
    global num;
    num=e.get()
    e.delete(0,END)
    global b;
    b=n 

def equal():
    global num;
    global b;
    num2=e.get()
    e.delete(0,END)
    if b=='+':
        ans=float(num)+float(num2)
    elif b=='-':
        ans=float(num)-float(num2)
    elif b=='*':
        ans=float(num)*float(num2)
    elif b=='/':
        ans=float(num)/float(num2)
    elif b=='%':
        ans=(float(num)/float(num2))*100
    e.insert(0,ans)


def del_one():
    string=str(e.get())
    string=string[0:len(string)-1]
    e.delete(0,END)
    e.insert(0,string)

button_ac=Button(root,text="C",padx=21,pady=15,bd=3,  bg="#000033",fg="white",font='sans 12 bold',command=func).grid(row=1,column=0)
button_del=Button(root,text="x",padx=22,pady=15,bd=3, bg="#000033",fg="white",font='sans 12 bold',command=del_one).grid(row=1,column=1)
button_per=Button(root,text="%",padx=19,pady=15,bd=3, bg="#000033",fg="white",font='sans 12 bold',command=lambda: funct('%')).grid(row=1,column=2)
button_7=Button  (root,text=7,padx=22,pady=15,bd=3,   bg="#000033",fg="white",font='sans 12 bold',command=lambda: fun(7)).grid(row=2,column=0)
button_8=Button  (root,text=8,padx=22,pady=15,bd=3,   bg="#000033",fg="white",font='sans 12 bold',command=lambda: fun(8)).grid(row=2,column=1)
button_9=Button  (root,text=9,padx=22,pady=15,bd=3,   bg="#000033",fg="white",font='sans 12 bold',command=lambda: fun(9)).grid(row=2,column=2)
button_4=Button  (root,text=4,padx=22,pady=15,bd=3,   bg="#000033",fg="white",font='sans 12 bold',command=lambda: fun(4)).grid(row=3,column=0)
button_5=Button  (root,text=5,padx=22,pady=15,bd=3,   bg="#000033",fg="white",font='sans 12 bold',command=lambda: fun(5)).grid(row=3,column=1)
button_6=Button  (root,text=6,padx=22,pady=15,bd=3,   bg="#000033",fg="white",font='sans 12 bold',command=lambda: fun(6)).grid(row=3,column=2)
button_1=Button  (root,text=1,padx=22,pady=15,bd=3,   bg="#000033",fg="white",font='sans 12 bold',command=lambda: fun(1)).grid(row=4,column=0)
button_2=Button  (root,text=2,padx=22,pady=15,bd=3,   bg="#000033",fg="white",font='sans 12 bold',command=lambda: fun(2)).grid(row=4,column=1)
button_3=Button  (root,text=3,padx=22,pady=15,bd=3,   bg="#000033",fg="white",font='sans 12 bold',command=lambda: fun(3)).grid(row=4,column=2)
button_0=Button  (root,text=0,padx=22,pady=15,bd=3,   bg="#000033",fg="white",font='sans 12 bold',command=lambda: fun(0)).grid(row=5,column=1)
button_add=Button(root,text="+",padx=24,pady=15,bd=3, bg="#000033",fg="white",font='sans 12 bold',command=lambda: funct('+')).grid(row=4,column=3)
button_diff=Button(root,text="-",padx=26,pady=15,bd=3,bg="#000033",fg="white",font='sans 12 bold',command=lambda: funct('-')).grid(row=3,column=3)
button_mul=Button(root,text="*",padx=26,pady=15,bd=3, bg="#000033",fg="white",font='sans 12 bold',command=lambda: funct('*')).grid(row=2,column=3)
button_div=Button(root,text="/",padx=27,pady=15,bd=3, bg="#000033",fg="white",font='sans 12 bold',command=lambda: funct('/')).grid(row=1,column=3)
button_dot=Button(root,text=".",padx=24,pady=15,bd=3, bg="#000033",fg="white",font='sans 12 bold',command=lambda: fun('.')).grid(row=5,column=2)

button_close=Button(root,text="close",padx=7,pady=15,bd=3,bg="#660000",fg="white",font='sans 12 bold',command=root.destroy).grid(row=5,column=0)
button_eq=Button(root,text="=",padx=24,pady=15,bg="#004C99",bd=3,fg="white",font='sans 12 bold',command=equal).grid(row=5,column=3)

root.mainloop()









