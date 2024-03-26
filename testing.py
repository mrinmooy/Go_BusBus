from tkinter import *

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
    def blink(label): label.config(text="Press Enter to Proceed" if label.cget("text") == "" else "", fg="red"); root.after(500,blink,label) 
    # the blinking label 'Enter to Proceed'
    label =  Label(root, font=('Ariel',20),bg='pink')
    # calls the blinking function
    blink(label)
    label.pack(pady=40)
    # function to close window
    def close_page(event):
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
    root.mainloop()


# calling welcoming page funtion  
welcome_page()

