from tkinter import *

root=Tk()

w,h=root.winfo_screenwidth(),root.winfo_screenheight()

root.geometry('%dx%d+0+0'%(w,h))

img=PhotoImage(file='Bus.png')

Label(root,image=img).grid(row=0,column=0,padx=w/2.5,columnspan=7)

Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font="Arial 24 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=400,columnspan=7,pady=40)
def booking():
    root.destroy()
    import Bus_Booking
def check():
    root.destroy()
    import Check_Booking
def add():
    root.destroy()
    import loginpage

Button(root,text='Seat Booking',bg='LightGreen',font="Arial 14 bold",command=booking).grid(row=5,column=1,padx=80,columnspan=2)

Button(root,text='Check Booked seat',bg='green2',font="Arial 14 bold",command=check).grid(row=5,column=2,padx=60,columnspan=3)

Button(root,text='Update Database',bg='green4',font="Arial 14 bold",command=add).grid(row=5,column=3,columnspan=4)

Label(root,text="").grid(row=6,column=2)

admin=Label(root,text="For Admin Only",fg="red",font="Arial 8 bold").grid(row=7,column=3,columnspan=4)



