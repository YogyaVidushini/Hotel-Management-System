import tkinter as tk

def staff_dash():
    staff_dash=tk.Tk()
    staff_dash.title('ADMIN')
    staff_dash.geometry('1000x1000')
    staff_dash.configure(bg='grey')

    main_label=tk.Label(staff_dash, text="HOTEL STAFF",fg='black', bg="grey", font=("Times New Roman", 30, "bold"),height=1)
    main_label.grid(row=0,column=0,padx=10, pady=10)

    log_out= tk.Button(staff_dash,text="LOG OUT",bg='red',fg='red',font=('Times New Roman',15,"bold"), width=15)
    log_out.grid(row=0, column=4, padx=5, pady=5, sticky ='e')

    button_frame = tk.Frame(staff_dash,bg='grey',padx=10, pady=10, height=6)
    button_frame.grid(row=1, column=0, columnspan=5, pady=20)



    change_password= tk.Button(button_frame,text="Reset Password",width=15)
    change_password.grid(row=1, column=0, padx=5, pady=5)

    """view_staff= tk.Button(button_frame,text="View hotel staff",width=15)
    view_staff.grid(row=1, column=1,padx=5, pady=5)"""

    view_bookings= tk.Button(button_frame,text="View Bookings",width=15)
    view_bookings.grid(row=1, column=2, padx=5, pady=5)

    """add_room= tk.Button(button_frame,text="Add Rooms",width=15)
    add_room.grid(row=1, column=3, padx=5, pady=5)
    
    view_room= tk.Button(button_frame,text="View Rooms",width=15)
    view_room.grid(row=1, column=4, padx=5, pady=5)"""

    #configure row and columns to expand
    staff_dash.grid_rowconfigure(0, weight=2)
    staff_dash.grid_rowconfigure(1, weight=2)
    staff_dash.grid_rowconfigure(2, weight=2)
    staff_dash.grid_columnconfigure(1, weight=2)
    staff_dash.grid_columnconfigure(2, weight=2)
    """staff_dash.grid_columnconfigure(3, weight=2)
    staff_dash.grid_columnconfigure(4, weight=2)"""

    wel_label=tk.Label(staff_dash,text="WELCOME",fg='white',bg='grey', font=("Times New Roman", 60,"bold"),height=5)
    wel_label.grid(row=2, columnspan=5, pady=10, sticky='ew')


    staff_dash.mainloop()
