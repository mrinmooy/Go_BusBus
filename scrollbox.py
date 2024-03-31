from tkinter import *
from databaseFunctions import *

root = Tk()
root.state("zoomed")

Frame1 = Frame(root,bg='pink')
Frame1.pack(fill='both', expand=True)

Button(Frame1, text='Back').place(x=10,y=10)

From = "Bhopal"
To = "Jabalpur"
dateOfJourney = "30-03-2024"

Label(Frame1,text=From).place(x=500,y=100)
Label(Frame1,text=To).place(x=750,y=100) 
Label(Frame1,text=dateOfJourney).place(x=1000,y=100) 


main_frame = Frame(Frame1, bg='lightgray')
main_frame.place(x=400, y=200, width=800, height=500)

canvas = Canvas(main_frame, width=782, height=500, bg='lightgray')
scrollbar = Scrollbar(main_frame, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
canvas.place(x=0, y=0)
scrollbar.place(x=782, y=0, height=500)

labels_frame = Frame(canvas, bg="lightgray")

busDetails = findBusDetails(dateOfJourney, From, To)

# print(busDetails)

FrameX = Frame(labels_frame)
FrameX.pack(side=TOP)

Label(FrameX, text="Bus Operator").pack(side=LEFT)
Label(FrameX, text="Departure From").pack(side=LEFT)
Label(FrameX, text="Final Stop At").pack(side=LEFT)
Label(FrameX, text="Seats Available").pack(side=LEFT)


for i in busDetails: 
    # Label(labels_frame, text=f"{i}", bg="lightgray").pack()
    FrameX = Frame(labels_frame)
    FrameX.pack(side=TOP)
    Label(FrameX, text=f"{i[0]}").pack(side=LEFT)
    Label(FrameX, text=f"{i[1]}").pack(side=LEFT)
    Label(FrameX, text=f"{i[2]}").pack(side=LEFT)
    Label(FrameX, text=f"{i[3]}").pack(side=LEFT)
    Button(FrameX,text="Book Now").pack(side=LEFT)

canvas.create_window((0, 0), window=labels_frame, anchor="nw")
labels_frame.update_idletasks()  
canvas.config(scrollregion=canvas.bbox("all"))  
root.mainloop()
