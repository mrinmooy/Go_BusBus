from tkinter import *
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

img=PhotoImage(file="/Users/pravin/Desktop/Python/Bus.png")
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

Frame4=Frame(root)
Frame4.grid(row=8,column=0,columnspan=10)
Label(Frame4,text="Bus ID").grid(row=8,column=2,sticky=E)
Entry(Frame4).grid(row=8,column=3,sticky=W)

Label(Frame4,text="Running Date").grid(row=8,column=4,sticky=E)
Entry(Frame4).grid(row=8,column=5,sticky=W)

Label(Frame4,text="Seat Available").grid(row=8,column=6,sticky=E)
Entry(Frame4).grid(row=8,column=7,sticky=W)

Button(Frame4,text="Add Run",bg="light green",font="Arial 10 bold").grid(row=8,column=8,sticky=W)

Button(Frame4,text="Delete Run",bg="light green",font="Arial 10 bold").grid(row=8,column=9,sticky=W)

snap=PhotoImage(file="/Users/pravin/Desktop/Python/home.png")

Button(Frame4,image=snap).grid(row=11,column=8,pady=20)
