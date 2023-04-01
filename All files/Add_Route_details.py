from tkinter import *
import sqlite3
from tkinter.messagebox import *
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
Label(Frame2,text="Online Bus Booking System ",fg="red",bg="light blue",font="Arial 16 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=400,columnspan=7)
Label(root,text="").grid(row=4,column=0)

Frame3=Frame(root)
Frame3.grid(row=5,column=0,columnspan=10)
Label(Frame3,text="Add Bus Route Details ",fg="green",font="Arial 13 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=400,columnspan=7)
Label(root,text="").grid(row=6,column=0)
Label(root,text="").grid(row=7,column=0)

last_entry2 = Label(root)
def add():
    global last_entry2
    con=sqlite3.connect('mydatabase.db')
    
    Frame6.grid_forget()
    
    cur=con.cursor()
    last_entry2.destroy()
    if(routeid.get()==""):
        showerror('Feild Missing','Please enter RouteID')
    elif(sid.get()==""):
        showerror('Feild Missing','Please enter StationID')
    elif(station.get()==""):
        showerror('Feild Missing','Please enter Station Name')
    else:
        try:
            int(routeid.get())
            if(int(routeid.get())<0 or int(routeid.get())>100):
                showerror('Range Error','Route ID out of range\nEnter route ID in given range')
                return
        except:
            showerror('Invalid Input','Route ID must be a number')
            routeid.delete(0,END)
            return
        try:
            int(sid.get())
            if(int(sid.get())<0 or int(sid.get())>10):
                showerror('Range Error','Station ID out of range\nEnter Station ID in given range')
                return
        except:
            showerror('Invalid Input','Station ID must be a number')
            sid.delete(0,END)
            return
        try:
            int(station.get())
            showerror('Invalid Station','Station Name cannot be numbers only')
            station.delete(0,END)
            return
        except:
            m=0
        sname = station.get().lower()
        
        cur.execute("Select rid,sid from route")

        rinfo = cur.fetchall()
        
        i=0
        for l in rinfo:
            if(int(routeid.get())==rinfo[i][0]):
                if(int(sid.get())==rinfo[i][1]):
                    showerror('Record Exist','Record already exist for given Route and Station ID')
                    return
            i=i+1
        
        cur.execute("INSERT INTO route VALUES(:rid, :sid, :sname)",
                    {
                        'rid': routeid.get(),
                        'sid': sid.get(),
                        'sname': sname
                    }
                    )
        showinfo('Success','Record added successfully...')

        Frame6.grid(row=10,column=0,columnspan=10)
        for widget in Frame6.winfo_children():
            widget.destroy()

        Label(Frame6,text='Route Info',fg='Red',bg='LightBlue1',font="Arial 18 bold",borderwidth=1,relief="ridge").grid(row=0,column=0,columnspan=10,pady=15)
        
        Label(Frame6,text='Route ID',fg='green3',font='Arial 14 bold').grid(row=1,column=0,padx=15)
        
        Label(Frame6,text='Station ID',fg='green3',font='Helvetica 14 bold').grid(row=1,column=2,padx=15)
        
        Label(Frame6,text='Station Name',fg='green3',font='Helvetica 14 bold').grid(row=1,column=4,padx=15)
        
        Label(Frame6,text= routeid.get()).grid(row=2,column=0,padx=20,pady=5)

        Label(Frame6,text= sid.get()).grid(row=2,column=2,padx=20,pady=5)

        Label(Frame6,text= station.get()).grid(row=2,column=4,padx=20,pady=5)
            
        
        con.commit()
        con.close()
        routeid.delete(0,END)
        sid.delete(0,END)
        station.delete(0,END)

def delete():
    global last_entry2
    con=sqlite3.connect('mydatabase.db')
    Frame6.grid_forget()
    cur=con.cursor()
    last_entry2.destroy()
    if(routeid.get()==""):
        showerror('Feild Missing','Please enter RouteID')
    elif(sid.get()==""):
        showerror('Feild Missing','Please enter StationID')
    else:

        try:
            int(routeid.get())
            if(int(routeid.get())<0 or int(routeid.get())>100):
                showerror('Range Error','Route ID out of range\nEnter route ID in given range')
                return
        except:
            showerror('Invalid Input','Route ID must be a number')
            routeid.delete(0,END)
            return
        try:
            int(sid.get())
            if(int(sid.get())<0 or int(sid.get())>10):
                showerror('Range Error','Station ID out of range\nEnter Station ID in given range')
                return
        except:
            showerror('Invalid Input','Station ID must be a number')
            sid.delete(0,END)
            return
        
        cur.execute("Select rid,sid,sname from route")

        rinfo = cur.fetchall()
        flag=0
        sname='t'
        i=0
        for l in rinfo:
            if(int(routeid.get())==rinfo[i][0]):
                if(int(sid.get())==rinfo[i][1]):
                    flag=1
                    sname=rinfo[i][2]
            i=i+1
        if(flag==0):
            showerror('Invalid Route','No Route exist for given Route and Staion ID')
            return
        
        cur.execute("DELETE FROM route WHERE rid=:rid and sid=:sid",
                        {
                            'rid': routeid.get(),
                            'sid': sid.get()
                        }
                        )
        showinfo('Success','Record Deleted successfully...')

        Frame6.grid(row=10,column=0,columnspan=10)
        for widget in Frame6.winfo_children():
            widget.destroy()

        Label(Frame6,text='Route Info',fg='Red',bg='LightBlue1',font="Arial 18 bold",borderwidth=1,relief="ridge").grid(row=0,column=0,columnspan=10,pady=15)
        
        Label(Frame6,text='Route ID',fg='green3',font='Arial 14 bold').grid(row=1,column=0,padx=15)
        
        Label(Frame6,text='Station ID',fg='green3',font='Helvetica 14 bold').grid(row=1,column=2,padx=15)
        
        Label(Frame6,text='Station Name',fg='green3',font='Helvetica 14 bold').grid(row=1,column=4,padx=15)
        
        Label(Frame6,text= routeid.get()).grid(row=2,column=0,padx=20,pady=5)

        Label(Frame6,text= sid.get()).grid(row=2,column=2,padx=20,pady=5)

        Label(Frame6,text= sname).grid(row=2,column=4,padx=20,pady=5)
        
        con.commit()
        con.close()
        routeid.delete(0,END)
        sid.delete(0,END)
        station.delete(0,END)

def rlimit(value):
    entry=len(routeid.get())
    if(entry>2):
        routeid.delete(2,END)

def slimit(value):
    entry=len(sid.get())
    if(entry>1):
        sid.delete(1,END)
      
Frame4=Frame(root)
Frame4.grid(row=7,column=0,columnspan=10)
Label(Frame4,text="Route ID").grid(row=8,column=0,sticky=E)
routeid=Entry(Frame4)
routeid.grid(row=8,column=1,sticky=W)
routeid.bind('<KeyPress>',rlimit)
Frame5=Frame(root)

Frame5.grid(row=8,column=0,columnspan=10,pady=30)

Frame6=Frame(root)

Frame6.grid(row=9,column=0,columnspan=10)



Label(Frame4,text="Station ID").grid(row=8,column=2,sticky=E)
sid=Entry(Frame4)
sid.grid(row=8,column=3,sticky=W)
sid.bind('<KeyPress>',slimit)
Label(Frame4,text="Station Name").grid(row=8,column=4,sticky=E)
station=Entry(Frame4)
station.grid(row=8,column=5,sticky=W)

Label(Frame4,text="Range : (1 - 100)",font='helvetica 11 bold italic').grid(row=9,column=1)
Label(Frame4,text="Range : (1 - 10)",font='helvetica 11 bold italic').grid(row=9,column=3)


Button(Frame5,text="Add Route",bg="light green",command=add).grid(row=0,column=1,padx=10)
Button(Frame5,text="Delete Route",bg="light green",fg="red",command=delete).grid(row=0,column=2,padx=10)
def home():
    root.destroy()
    import Main_Menu
pic=PhotoImage(file="home.png")
Button(Frame5,image=pic,command=home).grid(row=0,column=3,padx=10)
