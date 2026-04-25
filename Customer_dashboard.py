import tkinter as tk
from main_dashboard import main

def cust_dash():
    customer_dash=tk.Tk()
    customer_dash.title('CUSTOMER')
    customer_dash.geometry('1000x1000')
    customer_dash.configure(bg='blue')

    main_label=tk.Label(customer_dash, text="HOTEL STAFF",fg='white', bg="blue", font=("Times New Roman", 30, "bold"),height=1)
    main_label.grid(row=0,column=0,padx=10, pady=10)

    log_out= tk.Button(customer_dash,text="LOG OUT",bg='red',fg='red',font=('Times New Roman',15,"bold"), width=15, command=main)
    log_out.grid(row=0, column=4, padx=5, pady=5, sticky ='e')

    button_frame = tk.Frame(customer_dash,bg='blue',padx=10, pady=10, height=6)
    button_frame.grid(row=1, column=0, columnspan=5, pady=20)



    view_rooms= tk.Button(button_frame,text="View Rooms",width=15)
    view_rooms.grid(row=1, column=0, padx=5, pady=5)

    view_bookings= tk.Button(button_frame,text="View Bookings",width=15)
    view_bookings.grid(row=1, column=2, padx=5, pady=5)


    #configure row and columns to expand
    customer_dash.grid_rowconfigure(0, weight=2)
    customer_dash.grid_rowconfigure(1, weight=2)
    customer_dash.grid_rowconfigure(2, weight=2)
    customer_dash.grid_columnconfigure(1, weight=2)
    customer_dash.grid_columnconfigure(2, weight=2)
    """staff_dash.grid_columnconfigure(3, weight=2)
    staff_dash.grid_columnconfigure(4, weight=2)"""

    wel_label=tk.Label(customer_dash,text="WELCOME DEAR CUSTOMER",fg='white',bg='blue', font=("Times New Roman", 60,"bold"),height=2)
    wel_label.grid(row=1, columnspan=5, pady=10, sticky='ew')



    customer_dash.mainloop()
