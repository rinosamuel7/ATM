from tkinter import *
from tkinter.ttk import Combobox  
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql

db = pymysql.Connection(host = "localhost",user = "root", password="12345678")
cur = db.cursor()
cur.execute("create database bank")
cur.execute("use bank")
cur.execute("create table details(accnumber varchar(20),passwo varchar(20))")



f = Tk()
f.title("Welcome to HDFC Bank")
f.geometry("1200x800")

def sub():
    global bal
    
    if int(e7.get()) <= bal:
        bal-=int(e7.get())
        messagebox.showinfo("Debited", e7.get()+" rupees successfully debited from your account")
    else:
        messagebox.showerror("Error","Insufficient Balance!")
        
def add():
    global bal
    bal+=int(e8.get())
    messagebox.showinfo("Credited", e8.get()+" rupees successfully credited to your account")
 

def debit():
    global photo4,la,e7,bal
    f4 = Tk()
    f4.title("Debit")
    f4.geometry("600x600")

    img4 = Image.open("cash.jpg")
    photo4 = ImageTk.PhotoImage(img4,master=f4)

    la = Label(f4, image = photo4)
    la.place(width= 600, height = 600)

    l13 = Label(f4,text="Hi "+name+", Enter the amount",fg ="white",bg ="Blue",font="Cambria 20 bold")
    l13.place(x=150,y=150)

    e7 = Entry(f4,width=25)     
    e7.place(x=230,y=300)

    b6 = Button(f4,text="Withdraw",width=10,command = sub)
    b6.place(x=270,y=350)
    
def credit():
    global photo5,lab,bal,e8
    f5 = Tk()
    f5.title("Credit")
    f5.geometry("600x600")

    img5 = Image.open("cash.jpg")
    photo5 = ImageTk.PhotoImage(img5,master=f5)

    lab = Label(f5, image = photo5)
    lab.place(width= 600, height = 600)

    l14 = Label(f5,text="Hi "+name+", Enter the amount",fg ="white",bg ="Blue",font="Cambria 20 bold")
    l14.place(x=150,y=150)

    e8 = Entry(f5,width=25)     
    e8.place(x=230,y=300)

    b7 = Button(f5,text="Deposit",width=10,command = add)
    b7.place(x=270,y=350)

def checkbal():
    
    messagebox.showinfo("Current balance", str(bal)+" rupees is you balance")
    
    

def login():
    global photo3,lll,name,bal
    actNum = e5.get()
    logPin = e6.get()
    signPin = e4.get()
    name = e.get()
    
    cur.execute("select * from details")
    for i in cur:
        if i[0]==actNum and i[1]==logPin:
            f3 = Tk()
            f3.title("Welcome")
            f3.geometry("1100x600")

            img3 = Image.open("bank2.jpg")
            photo3 = ImageTk.PhotoImage(img3,master=f3)

            lll = Label(f3, image = photo3)
            lll.place(width= 1100, height = 600)

            l12 = Label(f3,text="Hi "+name+", How do you want to proceed?",fg ="white",bg ="Blue",font="Cambria 30 bold")
            l12.place(x=280,y=100)

            b3 = Button(f3,text="Withdraw",width=30,command = debit)
            b3.place(x=470,y=300)

            b4 = Button(f3,text="Deposit",width=30,command = credit)
            b4.place(x=470,y=400)

            b5 = Button(f3,text="Check Balance",width=30,command = checkbal)
            b5.place(x=470,y=500)
            
   

def signup():
    global photo2,ll,actNo,e5,e6,bal
    bal = int(e3.get())
    n = e.get()
    nn = n[0:3]
    p = e2.get()
    pp = p[0:3]
    actNo = nn+pp
    passw = e4.get()
    messagebox.showinfo("Account Number", "Please note your Account Number: "+actNo)

    query = "insert into details values(%s,%s)"    
    val = [actNo,passw]
    cur.execute(query,val)
    db.commit()
    
    f2 = Tk()
    f2.title("Login to HDFC")
    f2.geometry("1100x600")

    img2 = Image.open("bank2.jpg")
    photo2 = ImageTk.PhotoImage(img2,master=f2)

    ll = Label(f2, image = photo2)
    ll.place(width= 1100, height = 600)

    l8 = Label(f2,text="Login to your Account",fg ="white",bg ="Blue",font="Cambria 30 bold")
    l8.place(x=370,y=100)

    l9 = Label(f2,text="Enter your Account Number",fg ="red",bg ="light blue",font="Cambria 16 bold")
    l9.place(x=310,y=200)

    l10 = Label(f2,text="Enter your PIN",fg ="red",bg ="light blue",font="Cambria 16 bold")
    l10.place(x=310,y=300)

    e5 = Entry(f2,width=25) #acct no
    e5.place(x=700,y=200)

    e6 = Entry(f2,width=25)     #pin
    e6.place(x=700,y=300)

    b2 = Button(f2,text="Login",width=10,command = login)
    b2.place(x=550,y=380)


fra = Frame(f, width = 1100, height = 700, bg = "light blue")
fra.place(x = 50, y = 50)

img = ImageTk.PhotoImage(Image.open("bank2.jpg"))

l = Label(fra, image = img)
l.place(x=0,y=40)

l2 = Label(f,text="Welcome to HDFC",fg ="white",bg ="Blue",font="Cambria 30 bold")
l2.place(x=430,y=100)

l3 = Label(f,text="Enter your details to create an Account",fg ="black",bg ="light blue",font="Cambria 20 bold")
l3.place(x=350,y=200)

l4 = Label(f,text="Enter your Name",fg ="red",bg ="light blue",font="Cambria 16 bold")
l4.place(x=350,y=290)

l5 = Label(f,text="Enter your mobile number",fg ="red",bg ="light blue",font="Cambria 16 bold")
l5.place(x=350,y=380)

l6 = Label(f,text="Initial Deposit Amount",fg ="red",bg ="light blue",font="Cambria 16 bold")
l6.place(x=350,y=470)

l7 = Label(f,text="Create your pin",fg ="red",bg ="light blue",font="Cambria 16 bold")
l7.place(x=350,y=560)

e = Entry(f,width=25)
e.place(x=700,y=290)

e2 = Entry(f,width=25)
e2.place(x=700,y=380)

e3 = Entry(f,width=25) #deposit amount
e3.place(x=700,y=470)



e4 = Entry(f,width=25)   #pin
e4.place(x=700,y=560)

b = Button(f,text="Sign Up",width=10,command=signup)
b.place(x=580,y=620)


