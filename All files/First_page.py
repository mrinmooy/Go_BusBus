from tkinter import *

root=Tk()

w,h=root.winfo_screenwidth(),root.winfo_screenheight()

root.state('zoomed')

img=PhotoImage(file='Bus.png')

Label(root,image=img).pack()

Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font="Arial 24 bold").pack()

Label(root,text='Name : Pravin Kumar Jalodiya',fg='blue2',font="Arial 11 bold",pady=25).pack()

Label(root,text='Er : 211B221',fg='blue2',font="Arial 11 bold",pady=25).pack()

Label(root,text='Mobile : 82697282XX ',fg='blue2',font="Arial 11 bold",pady=25).pack()

Label(root,text='Submitted to : Dr. Mahesh Kumar and Dr. Nilesh Patel',fg='Red',bg='LightBlue1',font="Arial 15 bold").pack()

Label(root,text='Project Based Learning',fg='Red',font="Arial 13 bold").pack()

def nex(e=0):
    root.destroy()
    import Main_Menu
root.bind("<KeyPress>",nex)
