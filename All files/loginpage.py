from tkinter import *
import sqlite3
from tkinter.messagebox import *
root=Tk()

w,h=root.winfo_screenwidth(),root.winfo_screenheight()

root.geometry('%dx%d+0+0'%(w,h))

img=PhotoImage(file='Bus.png')

Frame1=Frame(root)

Frame1.grid(row=0,column=0,columnspan=10,padx=w/2.45)

Label(Frame1,image=img).grid(row=0,column=0,columnspan=7)

Label(Frame1,text='ADMIN LOGIN',fg='Red',bg='LightBlue1',font="Arial 24 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,columnspan=10,pady=10)

Frame2=Frame(root)
Frame2.grid(row=1,column=0,columnspan=10)

Label(Frame2,text="Enter your Credentials",fg="green",font="Arial 13 bold",borderwidth=1,relief="ridge").grid(row=0,column=0,columnspan=10,pady=10)

Label(Frame2,text="Username",font='helvetica 11').grid(row=1,column=0)

Label(Frame2,text="(case sensitive)",font='helvetica 9 italic').grid(row=1,column=2)

user=Entry(Frame2)

user.grid(row=1,column=1)

Label(Frame2,text="Password",font='helvetica 11').grid(row=2,column=0)

password=Entry(Frame2,show = '*')

password.grid(row=2,column=1)

def login():
    userw='pravin'
    passw='python3'
    error=0
    try:
        int(user.get())
        showerror('Invalid Username','Username cannot be only numbers')
        user.delete(0,END)
        return
    except:
        error=0
    if(user.get()==""):
        showerror('Invalid Action','Username Cannot be empty')
        return
    if(password.get()==""):
        showerror('Invalid Action','Please enter Password')
        return
    else:
        if(user.get()==userw):
            if(password.get()==passw):
                root.destroy()
                import Update_Database
            else:
                showerror('Invalid Credentials','Password incorrect\nPlease try again')
                return
        else:
            showerror('Invalid Credentials','Username incorrect\nPlease try again')
            return
def home():
    root.destroy()
    import Main_Menu
pic=PhotoImage(file="home.png")
Button(Frame2,image=pic,command=home).grid(row=4,column=1,pady=30)
           
Button(Frame2,text='Login',font='helvetica 13 italic',command=login).grid(row=3,column=1)
