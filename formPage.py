from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

def submit_form():
    # print("Submitted Information")
    # print(f"Name: {name_entry.get()}")
    # print(f"Phone: {phone_entry.get()}")
    # print(f"Age: {age_combobox.get()}")
    # print(f"Sex: {sex_combobox.get()}")
    if(name_entry.get()==""):
        showerror("Error","Name is required")
    elif(phone_entry.get()==""):
        showerror('Error','Phone number is required')
    else:
        showinfo('Seat booked', 'Congratulations! Your seat has been successfully booked.')


root = Tk()
root.state('zoomed')

def go_back():
    print('gone back')


Button(root,text='Cancel', command=go_back).place(x=10,y=10)

disclaimer_frame = Frame(root,height=200,width=550, borderwidth=3, relief='ridge')
disclaimer_frame.place(x=500,y=170)

Label(disclaimer_frame,text="This bus will").place(x=100,y=20)
Label(disclaimer_frame,text="Start from : Bhopal").place(x=100,y=40)
Label(disclaimer_frame,text="Stop at : Jabalpur").place(x=300,y=40)
Label(disclaimer_frame,text="You will").place(x=100,y=90)
Label(disclaimer_frame,text="Board at: Bhopal").place(x=100,y=110)
Label(disclaimer_frame,text="Get off at: Jabalpur").place(x=300,y=110)
Label(disclaimer_frame,text='Fair is Rs. 200').place(x=100,y=160)


main_frame = Frame(root, padx=10, pady=10, height=210, width=550, borderwidth=3, relief='ridge')
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

submit_button = Button(root, text="Submit & Book", command=submit_form)
submit_button.place(x=730,y=630)

root.mainloop()
