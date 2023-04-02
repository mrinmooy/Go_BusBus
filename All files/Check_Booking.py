from tkinter import *
import sqlite3
from tkinter.messagebox import *
root=Tk()

w,h=root.winfo_screenwidth(),root.winfo_screenheight()

root.geometry('%dx%d+0+0'%(w,h))

img=PhotoImage(file='Bus.png')

Frame1=Frame(root)

Frame1.grid(row=0,column=0,columnspan=10,padx=w/2.6)

Label(Frame1,image=img).grid(row=0,column=0,columnspan=7)

Label(Frame1,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font="Arial 24 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,columnspan=7,pady=10)

Label(Frame1,text="Check Your Booking",bg="light green",fg="green",font="Arial 13 bold",borderwidth=1,relief="ridge").grid(row=2,column=0,columnspan=7,pady=5)

Frame3=Frame(root,relief='groove',bd=5)


def display_ticket_frame():
    con = sqlite3.connect('mydatabase.db')
    
    cur = con.cursor()
    
    int(mobile.get())
    
    Frame3.grid(row=3,column=0,columnspan=10)
                
    cur.execute("SELECT * FROM bookinghistory where phone=:phone",
                {
                'phone': mobile.get()
                }
                )
    info = cur.fetchall()
    
    for widget in Frame3.winfo_children():
        widget.destroy()
    Label(Frame3,text='Passenger Name : '+info[0][1],font='Arial 13 bold').grid(row=0,column=0,sticky='w')

    Label(Frame3,text='Age : '+str(info[0][7]),font='Arial 13 bold').grid(row=1,column=0,sticky='w')

    Label(Frame3,text='Gender : '+info[0][6],font='Arial 13 bold').grid(row=2,column=0,sticky='w')

    Label(Frame3,text='Travel Date : '+info[0][4],font='Arial 13 bold').grid(row=0,column=2,sticky='w')

    Label(Frame3,text='Boarding Point : '+info[0][8],font='Arial 13 bold').grid(row=1,column=2,sticky='w')

    Label(Frame3,text='Booked On : '+info[0][5],font='Arial 13 bold').grid(row=2,column=2,sticky='w')

    Label(Frame3,text='Seats Booked : '+str(info[0][11]),font='Arial 13 bold').grid(row=3,column=2,sticky='w')

    Label(Frame3,text='Booking Ref : '+str(info[0][2]),font='Arial 13 bold').grid(row=3,column=0,sticky='w')

    Label(Frame3,text='Fare : '+str(info[0][10]),font='Arial 13 bold').grid(row=4,column=2,sticky='w')

    Label(Frame3,text='Destination : '+info[0][9],font='Arial 13 bold').grid(row=5,column=0,sticky='w')

    Label(Frame3,text='Phone : '+str(info[0][3]),font='Arial 13 bold').grid(row=4,column=0,sticky='w')

    Label(Frame3,text='* Total fare of '+str(info[0][10])+' /- to be paid at the time of boarding the bus',font='Arial 12 italic').grid(row=6,column=0,columnspan=10)

def destroy_ticket_frame():
    Frame3.grid_forget()
    
def ticket():

    con = sqlite3.connect('mydatabase.db')
    
    cur = con.cursor()
    response=0
    if(mobile.get()==""):
        showerror('Field Missing','Please enter your mobile number')
        destroy_ticket_frame()
    else:
        try:
            display_ticket_frame()
            mobile.delete(0,END)
        except:
            try:
                int(mobile.get())
                if(len(mobile.get())==10):
                   response = askyesno('No Booking Found','Would you like to book a bus?')
                   #if(response == 1):
                       #go to booking page
                   
                else:
                    showerror('Bad Request','Enter a 10 digit valid number\n Please try again...')
                destroy_ticket_frame()
                mobile.delete(0,END)
            except:
                showerror('Bad Request','Input must be a number\n Please try again...')
                destroy_ticket_frame()
                mobile.delete(0,END)
        con.close()
        if(response==1):
            root.destroy()
            import Bus_Booking
                
Frame2=Frame(root)
Frame2.grid(row=1,column=0,columnspan=10)
Label(Frame2,text="Enter Your Mobile No:").grid(row=1,column=0,sticky=W,padx=10,pady=20)
def limit(value):
    entry=mobile.get()
    if(len(entry)>9):
        mobile.delete(9,END)
mobile=Entry(Frame2)
mobile.grid(row=1,column=1,sticky=E,pady=20)
mobile.bind('<KeyPress>',limit)
Button(Frame2,text="Check Booking",font='helvetica 12',command=ticket).grid(row=1,column=2,padx=10,pady=20)

def home():
    root.destroy()
    import Main_Menu
photu=PhotoImage(file="home.png")
Button(Frame2,image=photu,command=home).grid(row=1,column=3,columnspan=10,pady=10)


