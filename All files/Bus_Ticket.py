from tkinter import *
import sqlite3
from tkinter.messagebox import *
root=Tk()

w,h=root.winfo_screenwidth(),root.winfo_screenheight()

root.geometry('%dx%d+0+0'%(w,h))

img=PhotoImage(file='Bus.png')

Frame1=Frame(root)

Frame1.grid(row=0,column=0,columnspan=10,padx=w/2.5)

Label(Frame1,image=img).pack()

Label(Frame1,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font="Arial 24 bold").pack()

con = sqlite3.connect('mydatabase.db')
    
cur = con.cursor()
    
Label(Frame1,text='Bus Ticket',fg='black',font="Arial 15 bold",pady=5).pack()

Frame2=Frame(root,relief='groove',bd=5)

Frame2.grid(row=1,column=0,columnspan=10,padx=w/2.5,pady=10)

con.commit()

cur.execute("SELECT count(*) FROM bookinghistory")

lastid = cur.fetchall()
print(lastid)

cur.execute("SELECT * FROM bookinghistory where bookingid=:lastid",
                {
                    'lastid': lastid[0][0]
                }
                )
info = cur.fetchall()
print(info)
for widget in Frame2.winfo_children():
    widget.destroy()
Label(Frame2,text='Passenger Name : '+info[0][1],font='Arial 13 bold').grid(row=0,column=0,sticky='w')

Label(Frame2,text='Age : '+str(info[0][7]),font='Arial 13 bold').grid(row=1,column=0,sticky='w')

Label(Frame2,text='Gender : '+info[0][6],font='Arial 13 bold').grid(row=2,column=0,sticky='w')

Label(Frame2,text='Travel Date : '+info[0][4],font='Arial 13 bold').grid(row=0,column=2,sticky='w')

Label(Frame2,text='Boarding Point : '+info[0][8],font='Arial 13 bold').grid(row=1,column=2,sticky='w')

Label(Frame2,text='Booked On : '+info[0][5],font='Arial 13 bold').grid(row=2,column=2,sticky='w')

Label(Frame2,text='Seats Booked : '+str(info[0][11]),font='Arial 13 bold').grid(row=3,column=2,sticky='w')

Label(Frame2,text='Booking Ref : '+str(info[0][2]),font='Arial 13 bold').grid(row=3,column=0,sticky='w')

Label(Frame2,text='Fare : '+str(info[0][10]),font='Arial 13 bold').grid(row=4,column=2,sticky='w')

Label(Frame2,text='Destination : '+info[0][9],font='Arial 13 bold').grid(row=5,column=0,sticky='w')

Label(Frame2,text='Phone : '+str(info[0][3]),font='Arial 13 bold').grid(row=4,column=0,sticky='w')

Label(Frame2,text='* Total fare of '+str(info[0][10])+' /- to be paid at the time of boarding the bus',font='Arial 12 italic').grid(row=6,column=0,columnspan=10)
def exitt():
    a=showinfo('Message','Thank you for using our platform!')
    root.destroy()
def home():
    root.destroy()
    import Main_Menu
Button(root,text='Exit',font='Times_new_roman 10',command=exitt).grid(row=7,column=1,columnspan=10)
photu=PhotoImage(file="home.png")
Button(root,image=photu,font='Times_new_roman 10',command=home).grid(row=7,column=0,columnspan=10
