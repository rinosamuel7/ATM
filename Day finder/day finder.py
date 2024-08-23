from tkinter import *
from tkinter.ttk import Combobox  
from tkinter import messagebox

f = Tk()
f.title("Day Finder")
f.geometry("600x600")

def findday():
    n = int(e.get())        #day
    n2 = com.get()
    one = ["Jan","Oct"]
    four = ["Feb","March","Nov"]
    zero = ["April","July"]
    two = ["May"]
    five = ["June"]
    three=["August"]
    six = ["Dec","Sept"]
    if n2 in one:
        n22 = 1
    elif n2 in four:
        n22 = 4
    elif n2 in zero:           #month code
        n22 = 0
    elif n2 in two:
        n22 = 2
    elif n2 in five:
        n22 = 5
    elif n2 in three:
        n22 = 3
    elif n2 in six:
        n22 = 6
    
    n3 = e2.get()
    n4 = int(n3[-2:])            #year
    n5 = n4//4                  #no of leap
    if int(n3) >= 1500 and int(n3) < 1600:
        n6 = 0
    elif int(n3) >= 1600 and int(n3) < 1700:
        n6 = 6
    elif int(n3) >= 1700 and int(n3) < 1800:
        n6 = 4
    elif int(n3) >= 1800 and int(n3) < 1900:        #century code 
        n6 = 2
    elif int(n3) >= 1900 and int(n3) < 2000:
        n6 = 0
    elif int(n3) >= 2000 and int(n3) < 2100:
        n6 = 6
    elif int(n3) >= 2100 and int(n3) < 2200:
        n6 = 4
    elif int(n3) >= 2200 and int(n3) < 2300:
        n6 = 2

    add = n+n22+n4+n5+n6
    odd = add%7
    

    if odd==1:
        messagebox.showinfo("Day","Given date falls on 'Sunday'")
    if odd==2:
        messagebox.showinfo("Day","Given date falls on 'Monday'")
    if odd==3:
        messagebox.showinfo("Day","Given date falls on 'Tuesday'")
    if odd==4:
        messagebox.showinfo("Day","Given date falls on 'Wednesday'")
    if odd==5:
        messagebox.showinfo("Day","Given date falls on 'Thursday'")
    if odd==6:
        messagebox.showinfo("Day","Given date falls on 'Friday'")
    if odd==0:
        messagebox.showinfo("Day","Given date falls on 'Satuarday'")
    

l2 = Label(f,text="Welcome to Day Finder",fg ="white",bg ="Blue",font="Cambria 25 bold")
l2.place(x=140,y=100)

l3 = Label(f,text="Enter your Date",fg ="black",bg ="light blue",font="Cambria 15 bold")
l3.place(x=170,y=200)

l4 = Label(f,text="Enter your month",fg ="black",bg ="light blue",font="Cambria 15 bold")
l4.place(x=170,y=250)

l5 = Label(f,text="Enter your year",fg ="black",bg ="light blue",font="Cambria 15 bold")
l5.place(x=170,y=300)


e = Entry(f,width=25)
e.place(x=350,y=205)

com = Combobox(f)
com["values"] =("select","Jan","Feb","March","April","May","June","July","August","Sept","Oct","Nov","Dec") 
com.current(0)
com.place(x= 350,y=255)

e2 = Entry(f,width=25)
e2.place(x=350,y=305)

b = Button(f,text="Find Day",width=10, command = findday)
b.place(x=270,y=380)


