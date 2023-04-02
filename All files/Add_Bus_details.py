from tkinter import *
from tkinter.messagebox import *
import sqlite3

root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

img=PhotoImage(file="Bus.png")
Frame1=Frame(root)
Frame1.grid(row=0,column=0,columnspan=10)
Label(Frame1,image=img).grid(row=0,column=0,padx=w/2.45,columnspan=7)
Label(root,text="").grid(row=1,column=0)

Frame2=Frame(root)
Frame2.grid(row=2,column=0,columnspan=10)
Label(Frame2,text="Online Bus Booking System ",fg="red",bg="light blue",font="Arial 16 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=w/2.45,pady=10,columnspan=7)
Label(root,text="").grid(row=4,column=0)

Frame3=Frame(root)
Frame3.grid(row=3,column=0,columnspan=10)
Label(Frame3,text="Add Bus Details ",fg="green",font="Arial 13 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=w/2.45,pady=10,columnspan=7)
Label(root,text="").grid(row=6,column=0)
Label(root,text="").grid(row=7,column=0)

last_entry1 = Label(root)
def add():
    global last_entry1
    con=sqlite3.connect('mydatabase.db')
    Frame5.grid_forget()
    cur=con.cursor()
    last_entry1.destroy()
    if(busid.get()==""):
        showerror('Feild Missing','Please enter BusID')
    elif(bus=="Select"):
        showerror('Feild Missing','Please seslect bus type')
    elif(capacity.get()==""):
        showerror('Feild Missing','Please enter capacity')
    elif(fare.get()==""):
        showerror('Feild Missing','Please enter fare')
    elif(rid.get()==""):
        showerror('Feild Missing','Please enter RouteID')
    elif(opid.get()==""):
        showerror('Feild Missing','Please enter OperatorID')
    else:
        try:
            int(busid.get())
            if(int(busid.get())>399 or int(busid.get())<300):
                showerror('Invalid BUS ID','Bus ID out of range\nTry again')
                busid.delete(0,END)
                return
        except:
            showerror('Invalid Bus ID','Bus ID must be a number')
            busid.delete(0,END)
            return
        try:
            int(capacity.get())
            if(int(capacity.get())<1):
                showerror('Invalid capacity','Please enter a valid capacity')
                capacity.delete(0,END)
                return
        except:
            showerror('Invalid Capacity','Capacity must be a number')
            capacity.delete(0,END)
            return
        try:
            int(fare.get())
            if(int(fare.get())<1):
                showerror('Invalid fare','Please enter a valid fare')
                fare.delete(0,END)
                return
        except:
            showerror('Invalid Fare','Fare must be a number')
            fare.delete(0,END)
            return
        try:
            int(opid.get())
            if(int(opid.get())>299 or int(opid.get())<200):
                showerror('Invalid Operator ID','Operator ID out of range\nTry again')
                opid.delete(0,END)
                return
        except:
            showerror('Invalid Operator ID','Operator ID must be a number')
            opid.delete(0,END)
            return

        try:
            int(rid.get())
            if(int(rid.get())<0 or int(rid.get())>100):
                showerror('Invalid Route ID','Route ID out of range\nTry again')
                rid.delete(0,END)
                return
        except:
            showerror('Invalid Route ID',' Route ID must be a number')
            rid.delete(0,END)
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
        if(int(opid.get()) not in idslist):
            showinfo('Invalid Operator','No such operator exist')
            opid.delete(0,END)
            return

        cur.execute("SELECT rid from route")

        rd=cur.fetchall()
        print(rd)
        rdlist=[]
        i=0
        for l in rd:
            rdlist.append(rd[i][0])
            i=i+1
        print(rdlist)
        if(int(rid.get()) not in rdlist):
            showinfo('Invalid Route','No such Route exist')
            rid.delete(0,END)
            return

        cur.execute("Select busid,rid from bus")

        exist = cur.fetchall()
        print(exist)
        i=0
        for l in exist:
            if(int(busid.get())==exist[i][0]):
                if(int(rid.get())==exist[i][1]):
                    showerror('Record Exist','Record already exist')
                    return
            i=i+1
            
        cur.execute("INSERT INTO Bus VALUES(:busid, :bustype, :capacity,:fare, :rid, :opid)",
                        {
                            'busid': busid.get(),
                            'capacity': capacity.get(),
                            'fare': fare.get(),
                            'rid': rid.get(),
                            'opid': opid.get(),
                            'bustype' : bus.get()
                        }
                        )
        showinfo('Success','Record added successfully...')

        Frame5.grid(row=10,column=0,columnspan=10)
        for widget in Frame5.winfo_children():
            widget.destroy()

        Label(Frame5,text='Record Added',fg='Red',bg='LightBlue1',font="Arial 18 bold",borderwidth=1,relief="ridge").grid(row=0,column=0,columnspan=10,pady=15)
        
        Label(Frame5,text='Bus ID',fg='green3',font='Arial 14 bold').grid(row=1,column=0,padx=15)
        
        Label(Frame5,text='Bus Type',fg='green3',font='Helvetica 14 bold').grid(row=1,column=2,padx=15)
        
        Label(Frame5,text='Capacity',fg='green3',font='Helvetica 14 bold').grid(row=1,column=4,padx=15)
        
        Label(Frame5,text='Fare',fg='green3',font='Helvetica 14 bold').grid(row=1,column=6,padx=15)
        
        Label(Frame5,text='Operator ID',fg='green3',font='Helvetica 14 bold').grid(row=1,column=8,padx=15)

        Label(Frame5,text='Route ID',fg='green3',font='Helvetica 14 bold').grid(row=1,column=10,padx=15)
        
        Label(Frame5,text= busid.get()).grid(row=2,column=0,padx=15,pady=5)

        Label(Frame5,text= bus.get()).grid(row=2,column=2,padx=15,pady=5)

        Label(Frame5,text= capacity.get()).grid(row=2,column=4,padx=15,pady=5)

        Label(Frame5,text= fare.get()).grid(row=2,column=6,padx=15,pady=5)

        Label(Frame5,text= opid.get()).grid(row=2,column=8,padx=15,pady=5)

        Label(Frame5,text= rid.get()).grid(row=2,column=10,padx=15,pady=5)
        
        con.commit()
        con.close()
        opid.delete(0,END)
        busid.delete(0,END)
        capacity.delete(0,END)
        fare.delete(0,END)
        rid.delete(0,END)
        bus.set("Select")

def edit():
    global last_entry1

    con=sqlite3.connect('mydatabase.db')

    cur=con.cursor()

    last_entry1.destroy()

    Frame5.grid_forget()
    
    if(busid.get()==""):
        showerror('Feild Missing','Please enter BusID')
    elif(bus=="Select"):
        showerror('Feild Missing','Please select bus type')
    elif(capacity.get()==""):
        showerror('Feild Missing','Please enter capacity')
    elif(fare.get()==""):
        showerror('Feild Missing','Please enter fare')
    elif(rid.get()==""):
        showerror('Feild Missing','Please enter RouteID')
    elif(opid.get()==""):
        showerror('Feild Missing','Please enter OperatorID')
    else:
        try:
            int(busid.get())
            if(int(busid.get())>399 or int(busid.get())<300):
                showerror('Invalid BUS ID','Bus ID out of range\nTry again')
                busid.delete(0,END)
                return
        except:
            showerror('Invalid Bus ID','Bus ID must be a number')
            busid.delete(0,END)
            return
        try:
            int(capacity.get())
            if(int(capacity.get())<1):
                showerror('Invalid capacity','Please enter a valid capacity')
                capacity.delete(0,END)
                return
        except:
            showerror('Invalid Capacity','Capacity must be a number')
            capacity.delete(0,END)
            return
        try:
            int(fare.get())
            if(int(fare.get())<1):
                showerror('Invalid fare','Please enter a valid fare')
                fare.delete(0,END)
                return
        except:
            showerror('Invalid Fare','Fare must be a number')
            fare.delete(0,END)
            return
        try:
            int(opid.get())
            if(int(opid.get())>299 or int(opid.get())<200):
                showerror('Invalid Operator ID','Operator ID out of range\nTry again')
                opid.delete(0,END)
                return
        except:
            showerror('Invalid Operator ID','Operator ID must be a number')
            opid.delete(0,END)
            return

        try:
            int(rid.get())
            if(int(rid.get())<0 or int(rid.get())>100):
                showerror('Invalid Route ID','Route ID out of range\nTry again')
                rid.delete(0,END)
                return
        except:
            showerror('Invalid Route ID',' Route ID must be a number')
            rid.delete(0,END)
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
        if(int(opid.get()) not in idslist):
            showinfo('Invalid Operator','No such operator exist')
            opid.delete(0,END)
            return

        cur.execute("SELECT rid from route")

        rd=cur.fetchall()
        print(rd)
        rdlist=[]
        i=0
        for l in rd:
            rdlist.append(rd[i][0])
            i=i+1
        print(rdlist)
        if(int(rid.get()) not in rdlist):
            showinfo('Invalid Route','No such Route exist')
            rid.delete(0,END)
            return

        cur.execute("SELECT BusID from Bus where busid = :busid",
                            {
                                'busid': busid.get()
                            }
                            )
        p = cur.fetchall()
        print(p)
        if(p==[]):
            showerror('Invalid Bus ID','No Record for this Bus ID exist')
            return

        try:
            cur.execute("UPDATE Bus set bustype=:bustype,capacity=:capacity,fare=:fare,rid=:rid,oid=:opid where BusID=:busid and rid=:rid",
                                {
                                    'busid': busid.get(),
                                    'capacity': capacity.get(),
                                    'fare': fare.get(),
                                    'rid': rid.get(),
                                    'opid': opid.get(),
                                    'bustype': bus.get()
                                }
                                )
        except:
            showerror('Invalid Update','Bad request\nCannot edit data')
            return
            
        showinfo('Success','Record edited successfully...')

        Frame5.grid(row=10,column=0,columnspan=10)
        for widget in Frame5.winfo_children():
            widget.destroy()

        Label(Frame5,text='Record Added',fg='Red',bg='LightBlue1',font="Arial 18 bold",borderwidth=1,relief="ridge").grid(row=0,column=0,columnspan=10,pady=15)
        
        Label(Frame5,text='Bus ID',fg='green3',font='Arial 14 bold').grid(row=1,column=0,padx=15)
        
        Label(Frame5,text='Bus Type',fg='green3',font='Helvetica 14 bold').grid(row=1,column=2,padx=15)
        
        Label(Frame5,text='Capacity',fg='green3',font='Helvetica 14 bold').grid(row=1,column=4,padx=15)
        
        Label(Frame5,text='Fare',fg='green3',font='Helvetica 14 bold').grid(row=1,column=6,padx=15)
        
        Label(Frame5,text='Operator ID',fg='green3',font='Helvetica 14 bold').grid(row=1,column=8,padx=15)

        Label(Frame5,text='Route ID',fg='green3',font='Helvetica 14 bold').grid(row=1,column=10,padx=15)
        
        Label(Frame5,text= busid.get()).grid(row=2,column=0,padx=15,pady=5)

        Label(Frame5,text= bus.get()).grid(row=2,column=2,padx=15,pady=5)

        Label(Frame5,text= capacity.get()).grid(row=2,column=4,padx=15,pady=5)

        Label(Frame5,text= fare.get()).grid(row=2,column=6,padx=15,pady=5)

        Label(Frame5,text= opid.get()).grid(row=2,column=8,padx=15,pady=5)

        Label(Frame5,text= rid.get()).grid(row=2,column=10,padx=15,pady=5)
            
        con.commit()
        con.close()
        opid.delete(0,END)
        busid.delete(0,END)
        capacity.delete(0,END)
        fare.delete(0,END)
        rid.delete(0,END)
        bus.set("Select")
def show():

    con=sqlite3.connect('mydatabase.db')

    cur=con.cursor()
    
    Frame5.grid_forget()
    if(busid.get()==""):
        showerror('Feild Missing','Please enter BusID')
        return
    else:
        try:
            int(busid.get())
            if(int(busid.get())>399 or int(busid.get())<300):
                showerror('Invalid BUS ID','Bus ID out of range\nTry again')
                busid.delete(0,END)
                return
        except:
            showerror('Invalid Bus ID','Bus ID must be a number')
            busid.delete(0,END)
            return

    
    cur.execute("SELECT busid from Bus where busid = :bus",
                            {
                                'bus': busid.get()
                            }
                            )
    p = cur.fetchall()
    print(p)
    if(p==[]):
        showerror('Invalid Bus ID','No Record for this Bus ID exist')
        return

    Frame5.grid(row=10,column=0,columnspan=10)
    for widget in Frame5.winfo_children():
            widget.destroy()

    Label(Frame5,text='Bus Info',fg='Red',bg='LightBlue1',font="Arial 18 bold",borderwidth=1,relief="ridge").grid(row=0,column=0,columnspan=10,pady=15)
    
    Label(Frame5,text='Bus ID',fg='green3',font='Arial 14 bold').grid(row=1,column=0,padx=15)
    
    Label(Frame5,text='Bus Type',fg='green3',font='Helvetica 14 bold').grid(row=1,column=2,padx=15)
    
    Label(Frame5,text='Capacity',fg='green3',font='Helvetica 14 bold').grid(row=1,column=4,padx=15)
    
    Label(Frame5,text='Fare',fg='green3',font='Helvetica 14 bold').grid(row=1,column=6,padx=15)
    
    Label(Frame5,text='Operator ID',fg='green3',font='Helvetica 14 bold').grid(row=1,column=8,padx=15)

    Label(Frame5,text='Route ID',fg='green3',font='Helvetica 14 bold').grid(row=1,column=10,padx=15)

    cur.execute("Select * from bus where busid=:bus",
                {
                    'bus': busid.get()
                })

    businfo = cur.fetchall()
    
    cur.execute("SELECT count(*) from bus where busid=:busid",
                {
                    'busid': busid.get()
                }
                )
    labels = cur.fetchall()

    enteries = labels[0][0]
    print(labels)
    counter=2
    t=0
    while(enteries!=0):

        Label(Frame5,text= businfo[t][0]).grid(row=counter,column=0,padx=15,pady=5)

        Label(Frame5,text= businfo[t][1]).grid(row=counter,column=2,padx=15,pady=5)

        Label(Frame5,text= businfo[t][2]).grid(row=counter,column=4,padx=15,pady=5)

        Label(Frame5,text= businfo[t][3]).grid(row=counter,column=6,padx=15,pady=5)

        Label(Frame5,text= businfo[t][4]).grid(row=counter,column=8,padx=15,pady=5)

        Label(Frame5,text= businfo[t][5]).grid(row=counter,column=10,padx=15,pady=5)

        counter=counter+1

        enteries=enteries-1

        t=t+1

        
def blimit(value):
    entry=busid.get()
    if(len(entry)>2):
        busid.delete(2,END)
def olimit(value):
    entry=opid.get()
    if(len(entry)>2):
        opid.delete(2,END)
def rlimit(value):
    entry=rid.get()
    if(len(entry)>2):
        rid.delete(2,END)
    
Frame4=Frame(root)
Frame4.grid(row=5,column=0,columnspan=10)
Label(Frame4,text="Bus ID").grid(row=5,column=0,sticky=E)
busid=Entry(Frame4,width=15)

Frame5=Frame(root)
Frame5.grid(row=6,column=0,columnspan=10)
Label(Frame4,text="Range : (300 - 399)",font='helvetica 11 bold italic').grid(row=6,column=1)
busid.grid(row=5,column=1,sticky=W)

busid.bind('<KeyPress>',blimit)

Label(Frame4,text="Bus Type").grid(row=5,column=2,sticky=E)
bus=StringVar()
bus.set("Select")
option=["AC 2x2","AC 3x2","Non AC 2x2","Non AC 3x2","AC Sleeper 2x1","Non AC Sleeper 2x1"]
menu=OptionMenu(Frame4,bus,*option)
menu.grid(row=5,column=3,sticky=E)

Label(Frame4,text="Capacity").grid(row=5,column=4,sticky=E)
capacity=Entry(Frame4,width=15)
capacity.grid(row=5,column=5,sticky=W)


Label(Frame4,text="Fare Rs").grid(row=5,column=6,sticky=E)
fare=Entry(Frame4,width=10)
fare.grid(row=5,column=7,sticky=W)

Label(Frame4,text="Operator ID").grid(row=5,column=8,sticky=E)
opid=Entry(Frame4,width=10)
Label(Frame4,text="Range : (200 - 299)",font='helvetica 11 bold italic').grid(row=6,column=7)
opid.grid(row=5,column=9,sticky=W)
opid.bind('<KeyPress>',olimit)
Label(Frame4,text="Route ID").grid(row=5,column=10,sticky=E)
rid=Entry(Frame4,width=10)
rid.grid(row=5,column=11,sticky=W)
Label(Frame4,text="Range : (1 - 100)",font='helvetica 11 bold italic').grid(row=6,column=11)
rid.bind('<KeyPress>',rlimit)
Label(Frame4,text="").grid(row=9,column=0)
Label(Frame4,text="").grid(row=10,column=0)

Button(Frame4,text="Add Bus",bg="light green",command=add).grid(row=11,column=4)

Button(Frame4,text="Edit Bus",bg="light green",command=edit).grid(row=11,column=5)

Button(Frame4,text="Show Bus",bg="light green",command=show).grid(row=11,column=6)
def home():
    root.destroy()
    import Main_Menu
photu=PhotoImage(file="home.png")
Button(Frame4,image=photu,command=home).grid(row=11,column=7,padx=10)




