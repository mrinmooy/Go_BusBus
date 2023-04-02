from tkinter import *
import sqlite3
from tkinter.messagebox import *
import random
from datetime import date
from datetime import datetime
root=Tk()

w,h=root.winfo_screenwidth(),root.winfo_screenheight()

root.geometry('%dx%d+0+0'%(w,h))

img=PhotoImage(file='Bus.png')

Label(root,image=img).grid(row=0,column=0,padx=w/2.45,columnspan=7)

Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font="Arial 24 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=400,columnspan=7,pady=10)

Label(root,text="Enter Journey Details",bg="light green",fg="green",font="Arial 13 bold",borderwidth=1,relief="ridge").grid(row=3,column=0,columnspan=7)

Label(root,text="").grid(row=4,column=0)

Frame2=Frame(root)

Frame3=Frame(root)

check = 0
    
def clicked(value):
    global check
    check = value
def datecheck(test):
    format = "%d/%m/%Y"
    res = True
    try:
            res = bool(datetime.strptime(test, format))
    except ValueError:
            res = False
    return res

def show():

    con = sqlite3.connect('mydatabase.db')

    global check

    check = 0

    cur = con.cursor()

    r=IntVar()
    Frame3.grid_forget()
    Frame2.grid(row=6,column=0,columnspan=10,pady=20)
    
    if(to.get()==""):
        showerror('Field Missing','Please enter your Destination')
        Frame2.grid_forget()
        Frame3.grid_forget()
    elif(frm.get()==""):
        showerror('Field Missing','Please enter your Boarding Location')
        Frame2.grid_forget()
        Frame3.grid_forget()
    elif(jdate.get()==""):
        showerror('Field Missing','Please enter your Journey Date')
        Frame2.grid_forget()
        Frame3.grid_forget()
    else:

        try:
            int(to.get())
            showerror('Invalid Input','Destination cannot be a number')
            to.delete(0,END)
            return
            int(frm.get())
            showerror('Invalid Input','Boarding Location cannot be a number')
            frm.delete(0,END)
            return
        except:
            m=0
        res=datecheck(jdate.get())
        if(res==True):
            datelist=jdate.get().split("/")
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

        tsname = to.get().lower()
        
        cur.execute("SELECT * FROM route where Sname=:to",
                    {
                        'to': tsname
                    }
                    )

        to_records = cur.fetchall()
        print(to_records)

        fname = frm.get().lower()
        
        if(to_records == []):
            showinfo('No Bus Found','Sorry, No buses are available for this route')
            to.delete(0,END)
            frm.delete(0,END)
            jdate.delete(0,END)
            Frame2.grid_forget()
            Frame3.grid_forget()
            return
        cur.execute("SELECT * FROM route where Sname=:frm",
                    {
                        'frm': fname
                    }
                    )
        
        frm_records = cur.fetchall()
        if(frm_records == []):
            showinfo('No Bus Found','Sorry, No buses are available for this route')
            to.delete(0,END)
            frm.delete(0,END)
            jdate.delete(0,END)
            Frame2.grid_forget()
            Frame3.grid_forget()
            return
        i=0
        j=0
        tempid=0
        for record in to_records:
            for rec in frm_records:    
                if(to_records[i][0]==frm_records[j][0]):
                    if(to_records[i][1]>frm_records[j][1]):
                        tempid = to_records[i][0]
                j=j+1
            i=i+1
            j=0
        if(tempid==0):
            showinfo('No Bus Found','Sorry, No buses are available')
            oid.delete(0,END)
            name.delete(0,END)
            address.delete(0,END)
            Frame2.grid_forget()
            Frame3.grid_forget()
            return
        cur.execute("SELECT * FROM running where BusID IN(select BusID from BUS where RID=:tempid) and date=:jdate and Available_seats>0",
                    {
                        'tempid': tempid,
                        'jdate': jdate.get()
                    }
                    )
        run_info = cur.fetchall()

        if(run_info==[]):
            showinfo('No Bus Found','Sorry, No buses are available')
            to.delete(0,END)
            frm.delete(0,END)
            jdate.delete(0,END)
            Frame2.grid_forget()
            Frame3.grid_forget()
            return
        for widget in Frame2.winfo_children():
            widget.destroy()

        Label(Frame2,text='Select Bus',fg='green3',font='Arial 15 bold').grid(row=0,column=0,padx=20)
        
        Label(Frame2,text='Operator',fg='green3',font='Helvetica 15 bold').grid(row=0,column=2,padx=20)
        
        Label(Frame2,text='Bus Type',fg='green3',font='Helvetica 15 bold').grid(row=0,column=4,padx=20)
        
        Label(Frame2,text='Available/Capacity',fg='green3',font='Helvetica 15 bold').grid(row=0,column=6,padx=20)
        
        Label(Frame2,text='Fare',fg='green3',font='Helvetica 15 bold').grid(row=0,column=8,padx=20)

        Button(Frame2,text='Proceed to Book',fg='black',bg='LightGreen',font='Arial 14 bold',command=book).grid(row=2,column=10,padx=20)

        cur.execute("SELECT count(*) FROM running where BusID IN(select BusID from BUS where RID=:tempid) and date=:jdate and Available_seats>0",
                    {
                        'tempid': tempid,
                        'jdate': jdate.get()
                    }
                    )
        no_of_labels = cur.fetchall()
        enteries = no_of_labels[0][0]
        counter=0
        while(enteries!=0):
            cur.execute("SELECT * FROM Bus where BusID=:busid",
                        {
                            'busid': run_info[counter][0]
                        }
                        )
            bus_info = cur.fetchall()

            cur.execute("SELECT Name from operator where OID=:oid",
                        {
                            'oid': bus_info[0][5]
                        }
                        )
            op_name = cur.fetchall()
            
            Radiobutton(Frame2,text='Bus '+str(counter+1),font='Helvetica 11',variable=r,value=counter+1,command=lambda : clicked(r.get())).grid(row=counter+1,column=0,padx=20,pady=5)
            
            Label(Frame2,text=op_name[0][0],fg='blue',font='Helvetica 12 italic').grid(row=counter+1,column=2,padx=20,pady=5)

            Label(Frame2,text=bus_info[0][1],fg='blue',font='Helvetica 12 bold').grid(row=counter+1,column=4,padx=20,pady=5)

            Label(Frame2,text=str(run_info[counter][2])+'/'+str(bus_info[0][2]),fg='blue',font='Helvetica 12 bold').grid(row=counter+1,column=6,padx=20,pady=5)

            Label(Frame2,text=bus_info[0][3],fg='blue',font='Helvetica 12 bold').grid(row=counter+1,column=8,padx=20,pady=5)

            counter=counter+1

            enteries=enteries-1

def book():
    global check
    if(check==0):
        showerror('Field Missing','Please select a bus')
        Frame3.grid_forget()
        return

    def confirm():
        con = sqlite3.connect('mydatabase.db')
        
        cur = con.cursor()
        
        if(cname.get()==""):
            showerror('Field Missing','Please enter Name')
        elif(gender.get()=="Select"):
            showerror('Field Missing','Please Select Gender')
        elif(mno.get()==""):
            showerror('Field Missing','Please enter Mobile Number')
        elif(cage.get()==""):
            showerror('Field Missing','Please enter Age')
        elif(cseat.get()==""):
            showerror('Field Missing','Please enter No of seats')
        else:
            try:
                global check
                try:
                    int(cname.get())
                    showerror('Invalid Name','Name cannot be numbers')
                    cname.delete(0,END)
                    return
                except:
                    m=0
                try:
                    int(mno.get())
                except:
                    showerror('Invalid Mobile','Please enter valid mobile number')
                    mno.delete(0,END)
                    return
                try:
                    int(cage.get())
                except:
                    showerror('Invalid Age','Please enter valid Age')
                    cage.delete(0,END)
                    return
                try:
                    int(cseat.get())
                except:
                    showerror('Invalid Seat','Please enter valid number of seats')
                    cseat.delete(0,END)
                    return

                if(len(mno.get())!=10):
                    showerror('Wrong Input','Please enter a valid 10 digit Mobile number')
                    mno.delete(0,END)
                    return
                if(int(cage.get())>130 or int(cage.get())<1):
                    showerror('Wrong Input','Please enter a valid Age')
                    cage.delete(0,END)
                    return

                tsname=to.get().lower()
                
                cur.execute("SELECT * FROM route where Sname=:to",
                        {
                            'to': tsname
                        }
                        )

                to_records = cur.fetchall()

                fname = frm.get().lower()
                
                cur.execute("SELECT * FROM route where Sname=:frm",
                            {
                                'frm': fname
                            }
                            )

                frm_records = cur.fetchall()
            
                i=0
                j=0
                tempid=0
                for record in to_records:
                    for rec in frm_records:    
                        if(to_records[i][0]==frm_records[j][0]):
                            if(to_records[i][1]>frm_records[j][1]):
                                tempid = to_records[i][0]
                        j=j+1
                    i=i+1
                    j=0

                cur.execute("SELECT * FROM running where BusID IN(select BusID from BUS where RID=:tempid) and date=:jdate and Available_seats>0",
                            {
                                'tempid': tempid,
                                'jdate': jdate.get()
                            }
                            )
                run_info = cur.fetchall()

                if(int(cseat.get())>run_info[check-1][2] or int(cseat.get())<1):
                    showerror('Invalid Input','Please enter a valid no. of seats')
                    cseat.delete(0,END)
                    return

                cur.execute("SELECT * FROM Bus where BusID=:busid",
                            {
                                'busid': run_info[check-1][0]
                            }
                            )

                bus_info = cur.fetchall()
                
                cur.execute("SELECT ref,phone FROM Bookinghistory")
                ref = cur.fetchall()
                h=0

                cur.execute("SELECT count(*) FROM bookinghistory")

                lastid = cur.fetchall()

                reference = lastid[0][0] + 1
                
                for ph in ref:
                    if(ref[h][1]==int(mno.get())):
                        showinfo('Record exist','Booking from this number already exist..')
                        return
                    h=h+1
                    
                choice=askyesno('Confimation','Your fare is '+str(int(cseat.get())*bus_info[0][3])+'\nConfirm booking?')
                

                cur.execute("INSERT INTO Bookinghistory(pname,ref,phone,travel_on,bookedon,gender,age,source,destination,fare,seats) VALUES(:pname, :ref, :phone,:travelon, :bookedon, :gender,:age,:source,:destination,:fare,:seat)",
                                {
                                    'pname': cname.get(),
                                    'ref': reference,
                                    'phone': mno.get(),
                                    'travelon': jdate.get(),
                                    'bookedon': date.today(),
                                    'gender': gender.get(),
                                    'age' : cage.get(),
                                    'source': fname,
                                    'destination': tsname,
                                    'fare': (int(cseat.get())*bus_info[0][3]),
                                    'seat': cseat.get()
                                }
                                )

                new=run_info[check-1][2]-int(cseat.get())
            
                cur.execute("UPDATE running set available_seats=:seat where busid=:busid and date=:jdate",
                        {
                            'seat': new,
                            'busid': bus_info[0][0],
                            'jdate': jdate.get()
                        }
                        )
                
                if(choice==1):
                    showinfo('Success','Seat booked!')
                    cname.delete(0,END)
                    cage.delete(0,END)
                    cseat.delete(0,END)
                    mno.delete(0,END)
                    gender.set("Select")
                    Frame3.grid_forget()
                    Frame2.grid_forget()
                    to.delete(0,END)
                    frm.delete(0,END)
                    jdate.delete(0,END)
                    con.commit()
                    root.destroy()
                    import Bus_Ticket

            except:
                showerror('Invalid Entry','Booking already exist or you may have entered wrong values\nPlease enter valid values...')
                cname.delete(0,END)
                cage.delete(0,END)
                cseat.delete(0,END)
                mno.delete(0,END)
                gender.set("Select")
                
            
        con.close()

    def mlimit(value):
        entry=mno.get()
        if(len(entry)>9):
            mno.delete(9,END)
    def alimit(value):
        entry=cage.get()
        if(len(entry)>2):
            cage.delete(2,END)
        
    Label(Frame3,text='Fill Passenger Details',fg='Red',bg='LightBlue1',font="Arial 21 bold",borderwidth=1,relief="ridge").grid(row=0,column=0,columnspan=10,pady=15)
    Frame3.grid(row=7,column=0,columnspan=10)
    Label(Frame3,text="Name",font='Arial 11 bold').grid(row=1,column=0)
    cname=Entry(Frame3)
    cname.grid(row=1,column=1)

    Label(Frame3,text="Gender",font='Arial 11 bold').grid(row=1,column=2)
    gender=StringVar()
    gender.set("Select")
    option=["Male","Female","Other"]
    menu=OptionMenu(Frame3,gender,*option)
    menu.grid(row=1,column=3)

    Label(Frame3,text="Mobile No",font='Arial 11 bold').grid(row=1,column=4)
    mno=Entry(Frame3)
    mno.grid(row=1,column=5)
    mno.bind('<KeyPress>',mlimit)

    Label(Frame3,text="Age",font='Arial 11 bold').grid(row=1,column=6)
    cage=Entry(Frame3,width=10)
    cage.grid(row=1,column=7)
    cage.bind('<KeyPress>',alimit)
    
    Label(Frame3,text="No Of Seats",font='Arial 11 bold').grid(row=1,column=8)
    cseat=Entry(Frame3,width=10)
    cseat.grid(row=1,column=9)

    Button(Frame3,text='Book Seat',fg="black",bg='white',font='Arial 15',command=confirm).grid(row=1,column=10,padx=10)

    
            

            

Frame1=Frame(root)
Frame1.grid(row=5,column=0,columnspan=10)
Label(Frame1,text="To",font='Times_New_Roman 14 bold').grid(row=5,column=1,sticky=E)
to=Entry(Frame1)
to.grid(row=5,column=2,sticky=W)


Label(Frame1,text="From",font='Times_New_Roman 14 bold').grid(row=5,column=3,sticky=E)
frm=Entry(Frame1)
frm.grid(row=5,column=4,sticky=W)


Label(Frame1,text="Journey Date",font='Times_New_Roman 14 bold').grid(row=5,column=5,sticky=E)
jdate=Entry(Frame1)
Label(Frame1,text='Format : (DD/MM/YYYY)',font='Helvetica 12 italic bold').grid(row=6,column=6)
jdate.grid(row=5,column=6,sticky=W)

def home():
    root.destroy()
    import Main_Menu
Button(Frame1,text="Show Bus",bg="SpringGreen3",font="Arial 14 bold",command=show).grid(row=5,column=7)
image=PhotoImage(file="home.png")
Button(Frame1,image=image,command=home).grid(row=5,column=8,columnspan=3)
