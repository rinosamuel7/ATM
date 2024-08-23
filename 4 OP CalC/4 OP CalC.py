from tkinter import *
from tkinter import ttk


f = Tk()
f.title("4 OP CalC")
f.geometry("500x500")

def summ():
    n1 = e1.get()
    n2 = e2.get()
    n3 = float(n1)+float(n2)
    l1 = Label(f,text="The addition of two numbers is "+str(n3),fg = "red",font = '18')
    l1.place(x=100,y=230)
def diff():
    n1 = e1.get()
    n2 = e2.get()
    n3 = float(n2)-float(n1)
    l2 = Label(f,text="The difference of two numbers is "+str(n3),fg = "red",font = '18')
    l2.place(x=100,y=250)
def mult():
    n1 = e1.get()
    n2 = e2.get()
    n3 = float(n1)*float(n2)
    l3 = Label(f,text="The multiplication of two numbers is "+str(n3),fg = "red",font = '18')
    l3.place(x=100,y=290)
def div():
    n1 = e1.get()
    n2 = e2.get()
    n3 = float(n2)/float(n1)
    l4 = Label(f,text=str(n1)+ " goes "+str(n3)+" times in "+ str(n2),fg = "red",font = '18')
    l4.place(x=100,y=320)
'''
def calc():
    if b.cget("text"):
        print("hi")
    if b2.cget("text"):
        print("hello")
'''

l = Label(f,text="Enter Your Numbers",font = '18')
l.place(x=160,y=30)


e1 = Entry(f,width=25)
e1.place(x=280,y=100)

e2 = Entry(f,width=25)
e2.place(x=70,y=100)



b = ttk.Button(f,text="Sum",width=10,command=summ)
b.place(x=110,y=150)


b2 = ttk.Button(f,text="Difference",width=10,command=diff)
b2.place(x=300,y=150)

b3 = ttk.Button(f,text="Multiply",width=10,command=mult)
b3.place(x=110,y=190)


b4 = ttk.Button(f,text="Divide",width=10,command=div)
b4.place(x=300,y=190)
print(b.cget("text"))
print(b2.cget("text"))
print(b3.cget("text"))
print(b4.cget("text"))




