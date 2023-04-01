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

Frame_3=Frame(root)
Frame_3.grid(row=5,column=0,columnspan=10)
Label(Frame_3,text="Add New Details to DataBase ",fg="green4",bg='light green',font="Arial 12 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=400,columnspan=7)
Label(root,text="").grid(row=6,column=0)

def newop():
    root.destroy()
    import Add_Operator_Details
def newbus():
    root.destroy()
    import Add_Bus_details
def newroute():
    root.destroy()
    import Add_Route_details
def newrun():
    root.destroy()
    import Add_Bus_Running_Details
Button(root,text="New Operator",bg="pale green",command=newop).grid(row=7,column=0,columnspan=7)

Button(root,text="New Bus",bg="salmon",command=newbus).grid(row=7,column=1,columnspan=7)

Button(root,text="New Route",bg="SteelBlue3",command=newroute).grid(row=7,column=2,columnspan=7)

Button(root,text="New Run",bg="MistyRose3",command=newrun).grid(row=7,column=3,columnspan=7)

