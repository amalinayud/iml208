import tkinter 
from tkinter import ttk
from tkinter import messagebox


def submit_registration():
    accepted = accept_var.get()

    if accepted=="Accepted": 
    #User info
        name = name_entry.get()
        title = title_combobox.get()

        if name and title:
            age = age_spinbox.get()
            faculty = faculty_entry.get()
            semester = semester_entry.get()
            no_matric = matric_number_entry.get()

            #Registration info
            registration_status = reg_status_var.get()
            equipment = equipment_combobox.get()
            amount = amount_spinbox.get()
            date = date_entry.get()

            print("Name:", name,) 
            print("Title: ", title)
            print("Age: ", age)
            print("Faculty: ", faculty)
            print ("Semester: ", semester)
            print("No.Matric: ", no_matric)
            print("# Equipment: ", equipment) 
            print("# Amount: ", amount)
            print("# Date: ", date)
            print("Registration status: ", registration_status )
            print("--------------------------------------------")
        else:
            tkinter.messagebox.showwarning(title="Error", message= "Name and Title are required !")
    else:
        tkinter.messagebox.showwarning(title= "Error", message="You have not accepted the terms")


window = tkinter.Tk()
window.title("Sport Equipment Registration Form")

frame = tkinter.Frame(window)
frame.pack()

#Saving User Info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row= 0, column=0, padx=20, pady=20)

name_label = tkinter.Label(user_info_frame, text= "Name")
name_label.grid(row=0, column=0)
name_entry = tkinter.Entry(user_info_frame)
name_entry.grid(row= 1, column= 0)

title_label= tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["Mr.", "Ms."])
title_label.grid(row= 0, column=1)
title_combobox.grid(row= 1, column= 1)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=100)
age_label.grid(row= 0, column= 2)
age_spinbox.grid(row= 1, column= 2)

faculty_label = tkinter.Label(user_info_frame, text="Faculty")
faculty_label.grid(row= 2, column= 0)
faculty_entry = tkinter.Entry(user_info_frame)
faculty_entry.grid(row= 3, column= 0)

semester_label = tkinter.Label(user_info_frame, text="Semester")
semester_label.grid(row= 2, column= 1 )
semester_entry = tkinter.Spinbox(user_info_frame, from_=1, to='Infinity')
semester_entry.grid(row= 3, column= 1)

matric_number_label = tkinter.Label(user_info_frame, text="No.Matric")
matric_number_label.grid(row=2 , column=2)
matric_number_entry = tkinter.Entry(user_info_frame)
matric_number_entry.grid(row= 3, column=2)


for widget in user_info_frame .winfo_children():
    widget.grid_configure(padx= 10, pady= 5)

#Saving Registration Details
registration_frame = tkinter.LabelFrame(frame)
registration_frame.grid(row= 1, column= 0, sticky="news", padx= 20, pady= 20)

registered_label = tkinter.Label(registration_frame, text="Registration Status")

reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(registration_frame, text="Currently Registered"
                                       , variable=reg_status_var, onvalue="Registered", offvalue="Not Registered")

registered_label.grid(row= 0, column=0)
registered_check.grid(row= 1, column= 0)

equipment_label = tkinter.Label(registration_frame, text="Equipment")
equipment_combobox = ttk.Combobox(registration_frame, values=["Soccer balls", "Goalkeeper Gloves", "Soccer Jersey and Shorts", "Basketballs", "Basketball Hoop and Nets", "Cones for Drills", "Volleyballs", "Volleyball Nets", "Knee Pads", "Badminton Rackets", "Shuttlecocks and Net", "Bicycle", "Bike Repair Tools" ] )
equipment_label.grid(row= 0, column= 1)
equipment_combobox.grid(row=1, column=1)

amount_label = tkinter.Label(registration_frame, text="Amount")
amount_spinbox = tkinter.Spinbox(registration_frame, from_=1, to='Infinity')
amount_label.grid(row= 0, column= 2)
amount_spinbox.grid(row= 1, column= 2)

date_label = tkinter.Label(registration_frame, text="Date")
date_entry = tkinter.Entry(registration_frame)
date_label.grid(row= 2, column= 1)
date_entry.grid(row= 3, column= 1)

for widget in registration_frame.winfo_children():
    widget.grid_configure(padx= 10, pady= 5)

#Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row= 2, column= 0, sticky="News", padx= 20, pady= 20)

accept_var = tkinter.StringVar(value= "Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text= "I accept the terms and conditions."
                                  , variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row= 0, column= 0)

# Button
button = tkinter.Button(frame, text="Submit registration", command=submit_registration)
button.grid(row=4, column=0, sticky="News", padx=20, pady=10)

window.mainloop()
