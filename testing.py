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

    root.state('zoomed')
    root.title('Go-BusBus')
    root.config(bg='pink')

    def back_button():
        root.destroy()
        main_menu()


    Frame_top = Frame(root,bg='pink')
    Frame_top.pack(anchor='n')
    Button(Frame_top, text='Back', command=back_button).pack(anchor='w', pady=10, padx = 10)

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
    Frame_top.pack(anchor='n')
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


    Frame_top = Frame(root,bg='pink')
    Frame_top.pack(anchor='n')
    Button(Frame_top, text='Back', command=back_button).pack(anchor='w', pady=10, padx = 10)


    root.mainloop()



# calling welcoming page funtion  
#welcome_page()

import sqlite3

def viewDB():
    conn = sqlite3.connect('GoBusBus.db')
    c = conn.cursor()
    query = """
    SELECT name from sqlite_master WHERE type='table';
    """
    c.execute(query)
    tables =  c.fetchall()
    print(f"""here are all the tables in GoBusBus.db  :""")
    for table in tables:
        print(table[0])
    print()
    conn.close()

def viewTable(table):
    conn = sqlite3.connect('GoBusBus.db')
    c = conn.cursor()
    query = f"""
    SELECT rowid,* FROM {table};
    """
    print(f"table {table}")
    c.execute(query)
    rows = c.fetchall()
    for row  in rows:
        print(row)
    conn.commit()
    conn.close()

def createTable(table,columns):
    conn = sqlite3.connect('GoBusBus.db')
    c = conn.cursor()
    columns= ', '.join(columns)
    query = f"""
    CREATE TABLE IF NOT EXISTS {table} ({columns});
    """
    c.execute(query)
    print(f"table {table} created successfully")
    conn.commit()
    conn.close()

def dropTable(table):
    conn = sqlite3.connect('GoBusBus.db')
    c = conn.cursor()
    query = f"""
    DROP TABLE IF EXISTS {table};
    """
    c.execute(query)
    print(f"table {table} has been deleted..")
    conn.commit()
    conn.close()

def insertVal(table,data):
    conn = sqlite3.connect('GoBusBus.db')
    c = conn.cursor()
    data = ','.join(data)
    query = f"""
    INSERT INTO {table} 
    VALUES ({data});
    """
    c.execute(query)
    print(f"data inserted in table {table}")
    conn.commit()
    conn.close()





# drop('newTable')
#viewTables()
#viewTables()
# display('newTable')
# insert('newTable',('"mrinmoy"',))

#columns = ('names TEXT PRIMARY KEY',)
#create('newTable',columns)
#viewTables()
#display('newTable')
# insert('newTable',("'mrinmoy'",))

