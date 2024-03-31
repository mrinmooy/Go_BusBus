from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from databaseFunctions import *
from tkcalendar import Calendar
import datetime 

def welcome_page():
    # creates instance of tkinter
    root  = Tk()
    # zooms it to full screen
    root.state("zoomed")
    # sets up the title of the window
    root.title('Go-BusBus')
    # changes background to pink
    root.configure(bg='pink')
    # writes 'Welcome to Go-BusBus' on top
    Label(root,text='Welcome to Go-BusBus',fg='blue2',bg='light blue',font="Arial 24 bold").pack(pady=25)
    # calculates total screen width and height of users computer to render image properly
    w,h=root.winfo_screenwidth(),root.winfo_screenheight()
    # setting up dimensions for the bus png
    ch = h/4
    cw = w/2.7
    # creates a canvas to render the png image on; did this to resolve background transparency conflicts when rendering directly
    canvas = Canvas(root, width=cw, height=ch, bg='light blue')
    canvas.pack()
    # gets the pic and pastes it on the canvas
    img=PhotoImage(file='cool-bus.png')
    canvas.create_image(cw/2, ch/2, image=img,anchor='center')
    # writes me and my buddy's names on the page
    Label(root,text='Founders : \n Pravin Kumar Jalodiya  & \n Mrinmoy Sadhukhan',fg='blue2',font="Arial 15 bold",bg='pink',pady=25).pack()
    # and our contact number
    Label(root,text='Contact Details : \n 82697282XX \n 82695806XX ',fg='blue2',font="Arial 15 bold",bg='pink',pady=0).pack()
    # blink function to make label blink
    def blink(label): 
        global after_id
        label.config(text="Press Enter to Proceed" if label.cget("text") == "" else "", fg="red") 
        after_id = root.after(500,blink,label) 

    # the blinking label 'Enter to Proceed'
    label =  Label(root, font=('Ariel',20),bg='pink')
    # calls the blinking function
    blink(label)
    label.pack(pady=40)
    # function to close window
    def close_page(event):
         root.after_cancel(after_id)
         root.destroy()
         main_menu()
    # binds that closing function to keypress 'enter'
    root.bind("<Return>",close_page)
    # starts running the tkinter window
    root.mainloop()

def main_menu():
    
    root = Tk()
    root.state('zoomed')
    root.title('Go-BusBus')
    root.configure(bg='pink')
    
    buttons_frame = Frame(root,bg='pink')
    picture_frame = Frame(root,bg='pink')

    buttons_frame.pack(anchor='w')
   # picture_frame.pack(side=LEFT)

   # Label(buttons_frame,text='top').pack(side=TOP)
    def book_button(): 
        root.destroy()
        book()
    def check_button(): 
        root.destroy()
        check()
    def update_button():
        root.destroy()
        update()
    
    Button(buttons_frame,text="Seat Booking", font = 'Arial 14 bold', bg = 'light blue', fg = 'blue2', command=book_button).pack(anchor='n', padx=200, pady = (200,0))
    Button(buttons_frame,text="Check Seat", font = 'Arial 14 bold', bg = 'light blue', fg = 'blue2', command=check_button).pack(anchor='n', padx=200, pady = (100,0))
    Button(buttons_frame,text="Update Database", font = 'Arial 14 bold', bg = 'light blue', fg = 'blue2', command=update_button).pack(anchor='n', padx=200, pady = (100,0))
    
    
    root.mainloop()

def book():                 

    root = Tk()

    root1 = Frame(root,bg='pink')
    root1.pack(fill='both', expand=True)

    root.state('zoomed')
    root.title('Go-BusBus')
    root.config(bg='pink')

    def back_button1():
        root.destroy()
        main_menu()

    # back button part
    Frame1 = Frame(root1, bg='pink')
    Frame1.pack(anchor='n', fill='x')
    Button(Frame1, text='Back', command=back_button1).pack(anchor='w', pady=10, padx=10)

    # Container for calendar and comboboxes
    container = Frame(root1, bg='pink')
    container.pack(anchor='n', fill='x')


    starting_points = ['Bhopal', 'Dewas', 'Guna', 'Gwalior', 'Hoshangabad', 'Indore', 'Itarsi', 'Jabalpur', 'Sehore', 'Ujjain']
    destinations = ['Bhopal', 'Dewas', 'Guna', 'Gwalior', 'Hoshangabad', 'Indore', 'Itarsi', 'Jabalpur', 'Sehore', 'Ujjain']

    # Comboboxes part
    Frame2 = Frame(container, bg='pink')
    Frame2.pack(side='left',padx=(380,50))
    Frame3 = Frame(container, bg='pink')
    Frame3.pack(side='left', padx=(70,30))
    Frame4 = Frame(container, bg='pink')
    Frame4.pack(side='left', padx=(50,0))

    # Create and place the starting point combobox
    start_label = Label(Frame2, text="Source:")
    start_label.pack( anchor='n')
    start_combobox = ttk.Combobox(Frame2, values=starting_points, state="readonly")
    start_combobox.pack(anchor='n')
    start_combobox.set('Bhopal')  # Set default value

    # Create and place the destination combobox
    dest_label = Label(Frame3, text="Destination:")
    dest_label.pack(anchor='n')
    dest_combobox = ttk.Combobox(Frame3, values=destinations, state="readonly")
    dest_combobox.pack(anchor='n')
    dest_combobox.set('Jabalpur')  # Set default value

    # calendar part

    From="" 
    To=""
    dateOfJourney=""
    
    def getDate():
        global dateOfJourney
        dateOfJourney =  cal.get_date()
        # print("Selected date is : ", dateChosen)
        date_label.config(text=dateOfJourney)
    Label(Frame4, text="Date of Journey").pack(anchor='n', pady=(200,0))
    date_label = Label(Frame4, text="", width=12)
    date_label.pack(anchor='w', padx = 100) 
    cal = Calendar(Frame4, selectmode='day', year=datetime.datetime.now().year, month=datetime.datetime.now().month, day=datetime.datetime.now().day, date_pattern="dd/mm/y")
    cal.pack(anchor='w',padx=(10,0))
    Button(Frame4, text="Select Date", command=getDate).pack(anchor='w',padx = (110,0))

    Frame5 = Frame(root1, bg='pink')
    Frame5.pack(anchor='n', fill='both', expand=True)

    
    def goToBusPage():
        global From, To, dateOfJourney
        From = start_combobox.get()
        To = dest_combobox.get()
        # print(From)
        # print(To)
        # print(dateOfJourney)
        root1.pack_forget()
        root2.pack(fill='both', expand=True)
        fun1()
  

    Button(Frame5, text='Show Buses', command=goToBusPage).pack(anchor='n', pady=50, padx=(0,80))

    root2 = Frame(root, bg='pink')
    root3 = Frame(root, bg = 'pink')

    def fun1():
        global From, To, dateOfJourney
        
        def back_button2():
            root2.pack_forget()
            root1.pack(fill='both', expand=True)
            for widget in root2.winfo_children():
                widget.destroy()
        
        Frame1 = Frame(root2,bg='pink')
        Frame1.pack(fill='both', expand=True)

        Button(Frame1, text='Back',command=back_button2).place(x=10,y=10)

        # From = "Bhopal"
        # To = "Jabalpur"
        # dateOfJourney = "30-03-2024"
        dateOfJourney = dateOfJourney.replace('/','-')

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

        def bookIt(busid, startPoint, endPoint,seats):
            global From, To, dateOfJourney
            root2.pack_forget()
            root3.pack(fill='both', expand=True)
            fun2(From,To,dateOfJourney,startPoint,endPoint,seats,busid)


        for i in busDetails: 
            # Label(labels_frame, text=f"{i}", bg="lightgray").pack()
            FrameX = Frame(labels_frame)
            FrameX.pack(side=TOP)
            Label(FrameX, text=f"{i[1]}").pack(side=LEFT)
            Label(FrameX, text=f"{i[2]}").pack(side=LEFT)
            Label(FrameX, text=f"{i[3]}").pack(side=LEFT)
            Label(FrameX, text=f"{i[4]}").pack(side=LEFT)
            Button(FrameX,text="Book Now",command=lambda i=i: bookIt(i[0], i[2], i[3], i[4])).pack(side=LEFT)

        canvas.create_window((0, 0), window=labels_frame, anchor="nw")
        labels_frame.update_idletasks()  
        canvas.config(scrollregion=canvas.bbox("all"))  
    
    def fun2(From, To, dateOfJourney, startPoint, endPoint, seats, busid):

        def submit_form():
            # print("Submitted Information")
            Name = name_entry.get()
            Phone = phone_entry.get()
            Age = age_combobox.get()
            Sex = sex_combobox.get()
            if(name_entry.get()==""):
                showerror("Error","Name is required")
            elif(phone_entry.get()==""):
                showerror('Error','Phone number is required')
            else:
                ticket = ticketMaker(busid,dateOfJourney,From,To,seats)
                insertVal('BookingLog',(dateOfJourney,busid,getCityID(From),getCityID(To)))
                insertVal('PassengerDetails',( ticket, Name,  Sex, Age, Phone))
                print(ticket)
                print(dateOfJourney)
                showinfo('Seat booked', 'Congratulations! Your seat has been successfully booked.')
                root.destroy()
                main_menu()


        

        def go_back():
            root3.pack_forget()
            root2.pack(fill='both', expand=True)
            for widget in root3.winfo_children():
                widget.destroy()


        Button(root3,text='Cancel', command=go_back).place(x=10,y=10)

        disclaimer_frame = Frame(root3,height=200,width=550, borderwidth=3, relief='ridge')
        disclaimer_frame.place(x=500,y=170)

        Label(disclaimer_frame,text="This bus will").place(x=100,y=20)
        Label(disclaimer_frame,text=f"Start from : {startPoint}").place(x=100,y=40)
        Label(disclaimer_frame,text=f"Stop at : {endPoint}").place(x=300,y=40)
        Label(disclaimer_frame,text="You will").place(x=100,y=90)
        Label(disclaimer_frame,text=f"Board at: {From}").place(x=100,y=110)
        Label(disclaimer_frame,text=f"Get off at: {To}").place(x=300,y=110)
        Label(disclaimer_frame,text='Fair is Rs. 200').place(x=100,y=160)


        main_frame = Frame(root3, padx=10, pady=10, height=210, width=550, borderwidth=3, relief='ridge')
        main_frame.place(x=500,y=400)

        Label(main_frame, text="Full Name:").place(x=100,y=10)
        name_entry = Entry(main_frame, width=30)
        name_entry.place(x=200,y=10)

        Label(main_frame, text="Phone Number:").place(x=100,y=60)
        phone_entry = Entry(main_frame, width=30)
        phone_entry.place(x=200,y=60)

        age_values = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42.43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]

        Label(main_frame, text="Age:").place(x=100,y=110)
        age_combobox = ttk.Combobox(main_frame, values=age_values, width=3, state="readonly")
        age_combobox.place(x=200,y=110)
        age_combobox.current(0) 
        Label(main_frame, text="Sex:").place(x=100,y=160)
        sex_combobox = ttk.Combobox(main_frame, values=["Male", "Female", "Other"], width=8, state="readonly")
        sex_combobox.place(x=200,y=160)
        sex_combobox.current(0)  

        submit_button = Button(root3, text="Submit & Book", command=submit_form)
        submit_button.place(x=730,y=630)

       

       


    



    root.mainloop()

def check():                 

    root = Tk()

    root.state('zoomed')
    root.title('Go-BusBus')
    root.config(bg='pink')

    def back_button():
        root.destroy()
        main_menu()


    Frame_top = Frame(root,bg='pink')
    Frame_top.pack(anchor='n', fill='x')
    Button(Frame_top, text='Back', command=back_button).pack(anchor='w', pady=10, padx = 10)


    root.mainloop()

def update():                 

    root = Tk()

    root.state('zoomed')
    root.title('Go-BusBus')
    root.config(bg='pink')

    def back_button():
        root.destroy()
        main_menu()


    Frame1 = Frame(root,bg='pink')
    Frame1.pack(anchor='n', fill='x')
    Button(Frame1, text='Back', command=back_button).pack(anchor='w', pady=10, padx = 10)

    

    root.mainloop()



# calling welcoming page funtion  
welcome_page()
# book()


# print(findBusDetails('29-03-2024','Dewas','Gwalior'))
# print(checkSeatAvailability('29-03-2024', 'ax04x084x1','B','D'))


