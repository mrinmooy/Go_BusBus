from tkinter import *
import sqlite3
from tkinter.messagebox import *
from datetime import date
from datetime import datetime

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
Label(Frame3,text="Add Bus Running Details ",fg="green",font="Arial 13 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=400,columnspan=7)
Label(root,text="").grid(row=6,column=0)
Label(root,text="").grid(row=7,column=0)

def datecheck(test):
    format = "%d/%m/%Y"
    res = True
    try:
            res = bool(datetime.strptime(test, format))
    except ValueError:
            res = False
    return res

def add():
    
    con=sqlite3.connect('mydatabase.db')
    Frame6.grid_forget()
    cur=con.cursor()
    if(busids.get()==""):
        showerror('Feild Missing','Please enter Bus ID')
    elif(rundate.get()==""):
        showerror('Feild Missing','Please enter running date')
    elif(seats.get()==""):
        showerror('Feild Missing','Please enter Station Name')
    else:
        
        try:
            int(busids.get())
            if(int(busids.get())<300 or int(busids.get())>399):
                showerror('Range Error','Please enter Bus ID in valid range')
                return
        except:
            showerror('Invalid Input','Bus ID must be number only')
            return

        res=datecheck(rundate.get())
        if(res==True):
            datelist=rundate.get().split("/")
            d = str(date.today())
            dlist=d.split("-")
            print(datelist)
            print(dlist)
            if(len(datelist[0])==2):
                if(len(datelist[1])==2):
                    m=0
                else:
                    showerror('Invalid month Format','Please enter month in correct format')
                    Frame2.grid_forget()
                    return
            else:
                showerror('Invalid date Format','Please enter date in correct format')
                Frame2.grid_forget()
                return
                    
            if(int(datelist[2])>int(dlist[0])):
                m=0
            elif(int(datelist[2])==int(dlist[0])):
                if(int(datelist[1])>int(dlist[1])):
                    m=0
                elif(int(datelist[1])==int(dlist[1])):
                    if(int(datelist[0])<int(dlist[2])):
                        showerror('Invalid Date','Please enter a valid date')
                        Frame2.grid_forget()
                        return
                else:
                    showerror('Invalid month','Please enter a valid month')
                    Frame2.grid_forget()
                    return
            else:
                showerror('Invalid Year','Please enter a valid Year')
                Frame2.grid_forget()
                return
        else:
            showerror('Wrong Date','Date or Date format incorrect\nTry again')
            Frame2.grid_forget()
            return

        cur.execute("Select capacity from bus where busid=:this",
                {
                    'this': busids.get()
                }
                )
        capa = cur.fetchall()
        print('capacity' + str(capa[0][0]))
        capci = capa[0][0]
                  
        try:
            int(seats.get())
            if(int(seats.get())>capci):
                showerror('ValueError','Available seats cannot exceed capacity')
                return
        except:
            showerror('Invalid Input','Seats must be number only')
            return

        try:
            cur.execute("INSERT INTO running VALUES(:busids, :rundate, :seats)",
                    {
                        'busids': busids.get(),
                        'rundate': rundate.get(),
                        'seats': seats.get()
                    }
                    )

        except:
            showinfo('Record Found','Bus is already running on this date')
            return
        
        showinfo('Success','Record added successfully...')

        Frame6.grid(row=10,column=0,columnspan=10)

        for widget in Frame6.winfo_children():
            widget.destroy()
            
        Label(Frame6,text='Added Record',fg='Red',bg='LightBlue1',font="Arial 18 bold",borderwidth=1,relief="ridge").grid(row=0,column=0,columnspan=10,pady=15)
        
        Label(Frame6,text='Bus ID',fg='green3',font='Arial 14 bold').grid(row=1,column=0,padx=20)
        
        Label(Frame6,text='Running Date',fg='green3',font='Helvetica 14 bold').grid(row=1,column=2,padx=20)
        
        Label(Frame6,text='Available seats',fg='green3',font='Helvetica 14 bold').grid(row=1,column=4,padx=20)
        
        
        Label(Frame6,text= busids.get()).grid(row=2,column=0,padx=20,pady=5)

        Label(Frame6,text= rundate.get()).grid(row=2,column=2,padx=20,pady=5)

        Label(Frame6,text= seats.get()).grid(row=2,column=4,padx=20,pady=5)


        con.commit()
        con.close()
        busids.delete(0,END)
        rundate.delete(0,END)
        seats.delete(0,END)

def delete():
    

    con=sqlite3.connect('mydatabase.db')

    cur=con.cursor()
    
    Frame6.grid_forget()
    
    if(busids.get()==""):
        showerror('Feild Missing','Please enter BusID')
    elif(rundate.get()==""):
        showerror('Feild Missing','Please enter Running Date')
    else:
        try:
            int(busids.get())
            if(int(busids.get())<300 or int(busids.get())>399):
                showerror('Range Error','Please enter Bus ID in valid range')
                return
        except:
            showerror('Invalid Input','Bus ID must be number only')
            return


        res=datecheck(rundate.get())

        if(res==True):
            datelist=rundate.get().split("/")
            d = str(date.today())
            dlist=d.split("-")
            print(datelist)
            print(dlist)
            if(len(datelist[0])==2):
                if(len(datelist[1])==2):
                    m=0
                else:
                    showerror('Invalid month Format','Please enter month in correct format')
                    Frame2.grid_forget()
                    return
            else:
                showerror('Invalid date Format','Please enter date in correct format')
                Frame2.grid_forget()
                return
                    
            if(int(datelist[2])>int(dlist[0])):
                m=0
            elif(int(datelist[2])==int(dlist[0])):
                if(int(datelist[1])>int(dlist[1])):
                    m=0
                elif(int(datelist[1])==int(dlist[1])):
                    if(int(datelist[0])<int(dlist[2])):
                        showerror('Invalid Date','Please enter a valid date')
                        Frame2.grid_forget()
                        return
                else:
                    showerror('Invalid month','Please enter a valid month')
                    Frame2.grid_forget()
                    return
            else:
                showerror('Invalid Year','Please enter a valid Year')
                Frame2.grid_forget()
                return
        else:
            showerror('Wrong Date','Date or Date format incorrect\nTry again')
            Frame2.grid_forget()
            return

        cur.execute("SELECT * from running WHERE BusID=:busids and Date=:run",
                            {
                                'busids': busids.get(),
                                'run': rundate.get()
                            })
        
        s = cur.fetchall()
        print(s)
        sea = s[0][2]
        try:
            cur.execute("DELETE FROM running WHERE BusID=:busids and Date=:rundate",
                            {
                                'busids': busids.get(),
                                'rundate': rundate.get()
                            })
        except:
            showerror('Record Not Found','No record exist for given data')
            return
        
        showinfo('Success','Record Deleted successfully...')

        
        
        
        
        Frame6.grid(row=10,column=0,columnspan=10)

        for widget in Frame6.winfo_children():
            widget.destroy()
            
        Label(Frame6,text='Added Record',fg='Red',bg='LightBlue1',font="Arial 18 bold",borderwidth=1,relief="ridge").grid(row=0,column=0,columnspan=10,pady=15)
        
        Label(Frame6,text='Bus ID',fg='green3',font='Arial 14 bold').grid(row=1,column=0,padx=20)
        
        Label(Frame6,text='Running Date',fg='green3',font='Helvetica 14 bold').grid(row=1,column=2,padx=20)
        
        Label(Frame6,text='Available seats',fg='green3',font='Helvetica 14 bold').grid(row=1,column=4,padx=20)
        
        
        Label(Frame6,text= busids.get()).grid(row=2,column=0,padx=20,pady=5)

        Label(Frame6,text= rundate.get()).grid(row=2,column=2,padx=20,pady=5)

        Label(Frame6,text= sea).grid(row=2,column=4,padx=20,pady=5)

        con.commit()
        con.close()
        busids.delete(0,END)
        rundate.delete(0,END)
        busids.delete(0,END)
def blimit(value):
    entry=len(busids.get())
    if(entry>2):
        busids.delete(2,END)
Frame4=Frame(root)
Frame4.grid(row=7,column=0,columnspan=10)
Label(Frame4,text="Bus ID").grid(row=8,column=2,sticky=E)
busids=Entry(Frame4)
busids.grid(row=8,column=3,sticky=W)
busids.bind('<KeyPress>',blimit)
Frame5=Frame(root)
Frame5.grid(row=8,column=0,columnspan=10,pady=30)

Frame6=Frame(root)
Frame6.grid(row=9,column=0,columnspan=10)


Label(Frame4,text="Range : (300 - 399)",font='helvetica 11 bold italic').grid(row=9,column=3)
Label(Frame4,text="Running Date").grid(row=8,column=4,sticky=E)
rundate=Entry(Frame4)
rundate.grid(row=8,column=5,sticky=W)
Label(Frame4,text='Format : (DD/MM/YYYY)',font='Helvetica 12 italic bold').grid(row=9,column=5)
Label(Frame4,text="Seat Available").grid(row=8,column=6,sticky=E)
seats=Entry(Frame4)
seats.grid(row=8,column=7,sticky=W)

Button(Frame5,text="Add Route",bg="light green",command=add).grid(row=0,column=1,padx=10)
Button(Frame5,text="Delete Route",bg="light green",fg="red",command=delete).grid(row=0,column=2,padx=10)
def home():
    root.destroy()
    import Main_Menu
pic=PhotoImage(file="home.png")
Button(Frame5,image=pic,command=home).grid(row=0,column=3,padx=10)
