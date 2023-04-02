from tkinter import *
from tkinter.messagebox import *
import sqlite3
import re

root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file="Bus.png")
Frame1=Frame(root)
Frame1.grid(row=0,column=0,columnspan=10)
Label(Frame1,image=img).grid(row=0,column=0,padx=w/2.45,columnspan=7)
Label(root,text="").grid(row=2,column=0)

Frame2=Frame(root)
Frame2.grid(row=3,column=0,columnspan=10)
Label(Frame2,text="Online Bus Booking System ",fg="red",bg="light blue",font="Arial 16 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=w/2.45,columnspan=7)
Label(root,text="").grid(row=4,column=0)

Frame3=Frame(root)
Frame3.grid(row=5,column=0,columnspan=10)
Label(Frame3,text="Add Bus Operator Details ",fg="green",font="Arial 13 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=2.45,columnspan=7)
Label(root,text="").grid(row=6,column=0)
Label(root,text="").grid(row=7,column=0)

last_entry = Label(root)
def add():
    global last_entry
    con=sqlite3.connect('mydatabase.db')
    Frame6.grid_forget()
    cur=con.cursor()
    last_entry.destroy()
    if(oid.get()==""):
        showerror('Feild Missing','Please enter OperatorID')
    elif(name.get()==""):
        showerror('Feild Missing','Please enter name')
    elif(address.get()==""):
        showerror('Feild Missing','Please enter address')
    elif(phone.get()==""):
        showerror('Feild Missing','Please enter phone')
    elif(email.get()==""):
        showerror('Feild Missing','Please enter email')
    else:
        def check(mail):
            like = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

            if(re.fullmatch(like, mail)):
                return True

            else:
                return False
        try:
            int(oid.get())
            if(int(oid.get())<200 or int(oid.get())>299):
                showerror('Invalid OID','Operator ID out of range\nPlease enter a valid ID')
                oid.delete(0,END)
                return
        except:
            showerror('Invalid OID','Operator ID must be a number')
            oid.delete(0,END)
            return
        try:
            int(phone.get())
            if(len(phone.get())!=10):
                showerror('Invalid Phone','Phone must be a 10 digit number\nPlease try again')
                phone.delete(0,END)
                return
        except:
            showerror('Invalid Phone','Phone must be a number')
            phone.delete(0,END)
            return
        try:
            int(name.get())
            showerror('Invalid Name','Name cannot be numbers only\nPlease try again')
            name.delete(0,END)
            return
        except:
            m=0
        try:
            int(address.get())
            showerror('Invalid Address','Address cannot be numbers only\Please try again')
            address.delete(0,END)
            return
        except:
            m=0

        verify = bool(check(email.get()))
        if(verify==False):
            showerror('Invalid Email','Please enter a valid email')
            email.delete(0,END)
            return

        cur.execute("SELECT oid FROM operator")

        ids=cur.fetchall()
        print(ids)
        idslist=[]
        i=0
        for l in ids:
            idslist.append(ids[i][0])
            i=i+1
        print(idslist)
        if(int(oid.get()) in idslist):
            showinfo('Record Already exist','Record for this Operator ID already exist')
            return
            
        cur.execute("INSERT INTO operator VALUES(:oid, :name, :address, :phone, :email)",
                {
                    'oid': oid.get(),
                    'name': name.get(),
                    'address': address.get(),
                    'phone': phone.get(),
                    'email': email.get()
                    
                }
                )
        showinfo('Success','Record added successfully...')

        Frame6.grid(row=10,column=0,columnspan=10)
        for widget in Frame6.winfo_children():
            widget.destroy()
        Label(Frame6,text='Record Added',fg='Red',bg='LightBlue1',font="Arial 18 bold",borderwidth=1,relief="ridge").grid(row=0,column=0,columnspan=10,pady=15)
        
        Label(Frame6,text='Operator ID',fg='green3',font='Arial 14 bold').grid(row=1,column=0,padx=20)
        
        Label(Frame6,text='Name',fg='green3',font='Helvetica 14 bold').grid(row=1,column=2,padx=20)
        
        Label(Frame6,text='Address',fg='green3',font='Helvetica 14 bold').grid(row=1,column=4,padx=20)
        
        Label(Frame6,text='Phone',fg='green3',font='Helvetica 14 bold').grid(row=1,column=6,padx=20)
        
        Label(Frame6,text='Email',fg='green3',font='Helvetica 14 bold').grid(row=1,column=8,padx=20)
        
        Label(Frame6,text= oid.get()).grid(row=2,column=0,padx=20,pady=5)

        Label(Frame6,text= name.get()).grid(row=2,column=2,padx=20,pady=5)

        Label(Frame6,text= address.get()).grid(row=2,column=4,padx=20,pady=5)

        Label(Frame6,text= phone.get()).grid(row=2,column=6,padx=20,pady=5)

        Label(Frame6,text= email.get()).grid(row=2,column=8,padx=20,pady=5)
        
        con.commit()
        con.close()
        oid.delete(0,END)
        name.delete(0,END)
        address.delete(0,END)
        phone.delete(0,END)
        email.delete(0,END)
def edit():
    global last_entry

    con=sqlite3.connect('mydatabase.db')

    cur=con.cursor()
    
    Frame6.grid_forget()
    
    last_entry.destroy
    
    if(oid.get()==""):
        showerror('Feild Missing','Please enter OperatorID')
    elif(name.get()==""):
        showerror('Feild Missing','Please enter name')
    elif(address.get()==""):
        showerror('Feild Missing','Please enter address')
    elif(phone.get()==""):
        showerror('Feild Missing','Please enter phone')
    elif(email.get()==""):
        showerror('Feild Missing','Please enter email')
    else:
        def check(mail):
            like = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

            if(re.fullmatch(like, mail)):
                return True

            else:
                return False
        try:
            int(oid.get())
            if(int(oid.get())>199 and int(oid.get())<300):
                m=0
            else:
                showerror('Invalid OID','Operator ID out of range\nPlease enter a valid ID')
                oid.delete(0,END)
                return
        except:
            showerror('Invalid OID','Operator ID must be a number')
            oid.delete(0,END)
            return
        try:
            int(phone.get())
            if(len(phone.get())==10):
                m=0
            else:
                showerror('Invalid Phone','Phone must be a 10 digit number\nPlease try again')
                phone.delete(0,END)
                return
        except:
            showerror('Invalid Phone','Phone must be a number')
            phone.delete(0,END)
            return
        try:
            int(name.get())
            showerror('Invalid Name','Name cannot be numbers only\nPlease try again')
            name.delete(0,END)
            return
        except:
            m=0
        try:
            int(address.get())
            showerror('Invalid Address','Address cannot be numbers only\Please try again')
            address.delete(0,END)
            return
        except:
            m=0

        verify = bool(check(email.get()))
        if(verify==False):
            showerror('Invalid Email','Please enter a valid email')
            email.delete(0,END)
            return
        cur.execute("SELECT oid from operator where oid = :oid",
                        {
                            'oid': oid.get()
                        }
                        )
        p = cur.fetchall()
        if(p==[]):
            showinfo('No record found','The record you want to edit does not exist\nTry again')
            return
        
        cur.execute("UPDATE operator set name=:name,address=:address,phone=:phone,email=:email where oid=:oid",
                            {
                                'oid': oid.get(),
                                'name': name.get(),
                                'address': address.get(),
                                'phone': phone.get(),
                                'email': email.get()
                                
                            }
                            )
        showinfo('Success','Record edited successfully...')

        Frame6.grid(row=10,column=0,columnspan=10)
        for widget in Frame6.winfo_children():
            widget.destroy()
        Label(Frame6,text='Record Edited',fg='Red',bg='LightBlue1',font="Arial 18 bold",borderwidth=1,relief="ridge").grid(row=0,column=0,columnspan=10,pady=15)
        
        Label(Frame6,text='Operator ID',fg='green3',font='Arial 14 bold').grid(row=1,column=0,padx=20)
        
        Label(Frame6,text='Name',fg='green3',font='Helvetica 14 bold').grid(row=1,column=2,padx=20)
        
        Label(Frame6,text='Address',fg='green3',font='Helvetica 14 bold').grid(row=1,column=4,padx=20)
        
        Label(Frame6,text='Phone',fg='green3',font='Helvetica 14 bold').grid(row=1,column=6,padx=20)
        
        Label(Frame6,text='Email',fg='green3',font='Helvetica 14 bold').grid(row=1,column=8,padx=20)
        
        Label(Frame6,text= oid.get()).grid(row=2,column=0,padx=20,pady=5)

        Label(Frame6,text= name.get()).grid(row=2,column=2,padx=20,pady=5)

        Label(Frame6,text= address.get()).grid(row=2,column=4,padx=20,pady=5)

        Label(Frame6,text= phone.get()).grid(row=2,column=6,padx=20,pady=5)

        Label(Frame6,text= email.get()).grid(row=2,column=8,padx=20,pady=5)
        
        
        con.commit()
        con.close()
        oid.delete(0,END)
        name.delete(0,END)
        address.delete(0,END)
        phone.delete(0,END)
        email.delete(0,END)
        
def show():
    con=sqlite3.connect('mydatabase.db')
    cur=con.cursor()
    Frame6.grid_forget()
    if(oid.get()==""):
        showerror('Feild Missing','Please enter OperatorID')
        return
    try:
        int(oid.get())
        if(int(oid.get())>199 and int(oid.get())<300):
            m=0
        else:
            showerror('Invalid OID','Operator ID out of range\nPlease enter a valid ID')
            oid.delete(0,END)
            return
    except:
        showerror('Invalid OID','Operator ID must be a number')
        oid.delete(0,END)
        return

    
    cur.execute("SELECT * from operator where oid = :oid",
                        {
                            'oid': oid.get()
                        }
                        )
    p = cur.fetchall()
    if(p==[]):
        showinfo('No record found','The record you want to see does not exist\nTry again')
        
        return
    else:
        Frame6.grid(row=10,column=0,columnspan=10)

        for widget in Frame6.winfo_children():
            widget.destroy()
            
        Label(Frame6,text='Requested Record',fg='Red',bg='LightBlue1',font="Arial 18 bold",borderwidth=1,relief="ridge").grid(row=0,column=0,columnspan=10,pady=15)
        
        Label(Frame6,text='Operator ID',fg='green3',font='Arial 14 bold').grid(row=1,column=0,padx=20)
        
        Label(Frame6,text='Name',fg='green3',font='Helvetica 14 bold').grid(row=1,column=2,padx=20)
        
        Label(Frame6,text='Address',fg='green3',font='Helvetica 14 bold').grid(row=1,column=4,padx=20)
        
        Label(Frame6,text='Phone',fg='green3',font='Helvetica 14 bold').grid(row=1,column=6,padx=20)
        
        Label(Frame6,text='Email',fg='green3',font='Helvetica 14 bold').grid(row=1,column=8,padx=20)
        
        Label(Frame6,text= str(p[0][0])).grid(row=2,column=0,padx=20,pady=5)

        Label(Frame6,text= p[0][1]).grid(row=2,column=2,padx=20,pady=5)

        Label(Frame6,text= p[0][2]).grid(row=2,column=4,padx=20,pady=5)

        Label(Frame6,text= str(p[0][3])).grid(row=2,column=6,padx=20,pady=5)

        Label(Frame6,text= p[0][4]).grid(row=2,column=8,padx=20,pady=5)

def olimit(value):
    entry=oid.get()
    if(len(entry)>2):
        oid.delete(2,END)
def plimit(value):
    entry=phone.get()
    if(len(entry)>9):
        phone.delete(9,END)
Frame4=Frame(root)
Frame4.grid(row=8,column=0,columnspan=10)

Frame5=Frame(root)
Frame5.grid(row=9,column=0,columnspan=10)

Frame6=Frame(root)
Frame6.grid(row=10,column=0,columnspan=10)
            
Label(Frame4,text="Operator ID").grid(row=8,column=0,sticky=E)

Label(Frame4,text="Range : (200 - 299)",font='helvetica 11 bold italic').grid(row=9,column=1)

oid=Entry(Frame4,width=15)

oid.grid(row=8,column=1,sticky=W)

oid.bind('<KeyPress>',olimit)
Label(Frame4,text="Name").grid(row=8,column=2,sticky=E)

name=Entry(Frame4)
name.grid(row=8,column=3,sticky=W)

Label(Frame4,text="Address").grid(row=8,column=4,sticky=E)

address=Entry(Frame4)
address.grid(row=8,column=5,sticky=E)

Label(Frame4,text="Phone").grid(row=8,column=6,sticky=E)

phone=Entry(Frame4)

phone.grid(row=8,column=7,sticky=W)

phone.bind('<KeyPress>',plimit)

Label(Frame4,text="Email").grid(row=8,column=8,sticky=W)

email=Entry(Frame4)
email.grid(row=8,column=8,padx=40)

Button(Frame5,text="Add",font="Helvetica 13",bg="light green",command=add).grid(row=0,column=1)

Button(Frame5,text="Edit",bg="light green",font="Helvetica 13",command=edit).grid(row=0,column=2,padx=20)

Button(Frame5,text="Show",font="Helvetica 13",bg="light green",command=show).grid(row=0,column=3)

Label(Frame4,text="").grid(row=10,column=0)

Label(Frame4,text="").grid(row=11,column=0)
def home():
    root.destroy()
    import Main_Menu
photu=PhotoImage(file="home.png")
Button(Frame5,image=photu,command=home).grid(row=0,column=4,columnspan=7,padx=10)


