from tkinter import *
from tkinter import ttk
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

    starting_points = ['Bhopal', 'Dewas', 'Guna', 'Gwalior', 'Hoshingabad', 'Indore', 'Itarsi', 'Jabalpur', 'Sehore', 'Ujjain']
    destinations = ['Bhopal', 'Dewas', 'Guna', 'Gwalior', 'Hoshingabad', 'Indore', 'Itarsi', 'Jabalpur', 'Sehore', 'Ujjain']

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
    start_combobox.set('Select Source City')  # Set default value

    # Create and place the destination combobox
    dest_label = Label(Frame3, text="Destination:")
    dest_label.pack(anchor='n')
    dest_combobox = ttk.Combobox(Frame3, values=destinations, state="readonly")
    dest_combobox.pack(anchor='n')
    dest_combobox.set('Select Destination City')  # Set default value

    # calendar part
    
    def getDate():
        dateChosen = cal.get_date()
        print("Selected date is : ", dateChosen)
        date_label.config(text=dateChosen)
    Label(Frame4, text="Date of Journey").pack(anchor='n', pady=(200,0))
    date_label = Label(Frame4, text="", width=12)
    date_label.pack(anchor='w', padx = 100) 
    cal = Calendar(Frame4, selectmode='day', year=datetime.datetime.now().year, month=datetime.datetime.now().month, day=datetime.datetime.now().day, date_pattern="dd/mm/y")
    cal.pack(anchor='w',padx=(10,0))
    Button(Frame4, text="Select Date", command=getDate).pack(anchor='w',padx = (110,0))

    Frame5 = Frame(root1, bg='pink')
    Frame5.pack(anchor='n', fill='both', expand=True)

    def goToBusPage():
        root1.pack_forget()
        root2.pack(fill='both', expand=True)


    Button(Frame5, text='Show Buses', command=goToBusPage).pack(anchor='n', pady=50, padx=(0,80))

    root2 = Frame(root, bg='pink')

    def back_button2():
        root2.pack_forget()
        root1.pack(fill='both', expand=True)

   
    Frame1 = Frame(root2, bg='pink')
    Frame1.pack(anchor='n', fill='x')
    Button(Frame1, text='Back', command=back_button2).pack(anchor='w', pady=10, padx=10)


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
# welcome_page()
book()


# print(findBusDetails('29-03-2024','Dewas','Gwalior'))
# print(checkSeatAvailability('29-03-2024', 'ax04x084x1','B','D'))


