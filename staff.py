import tkinter as tk

def view_booking():
    view_booking=tk.Tk()
    view_booking.title('View Booking')
    view_booking.geometry('500x500')
    view_booking.configure(bg='lightblue')

    # Heading label
    label_top = tk.Label(view_booking, text="View Bookings", bg='lightblue', font=("Times New Roman", 25, 'bold'))
    label_top.grid(row=0, column=0, columnspan=2, pady=10)

    # choose date label
    date = tk.Label(view_booking, text="  Choose Date  : ").grid(row=1, column=0, padx=10, pady=5, sticky='e')

    # textbox for amount
    entry_date = tk.Entry(view_booking)
    entry_date.grid(row=1, column=1)

    # button implementation
    assign_button = tk.Button(view_booking, text="Assign Rooms", fg='blue', command=lambda: final_assign(view_booking))
    assign_button.grid(row=3, column=0, columnspan=2, pady=10)

    view_booking.mainloop()

def final_assign(view_booking):
    # Destroy the billing window when the add bill window opens
    view_booking.destroy()

    final_assign = tk.Toplevel()
    final_assign.title('Assign rooms')
    final_assign.geometry('500x250')

    # amount label
    checkin_date_time = tk.Label(final_assign, text="  Check-in Date & Time   : ").grid(row=1, column=0, padx=10, pady=5, sticky='e')

    # textbox for amount
    entry_checkin_date_time = tk.Entry(final_assign)
    entry_checkin_date_time.grid(row=1, column=1)

    # create an IntVar instance
    check_var1 = tk.IntVar()
    check_var2 = tk.IntVar()

    # create a checkbutton widget and binds the command to print the check values
    checkbutton1 = tk.Checkbutton(final_assign, text="S1", variable=check_var1, onvalue=1)
    checkbutton1.grid(row=2, column=0, padx=10, pady=5)


    checkbutton2 = tk.Checkbutton(final_assign, text="S2", variable=check_var2, onvalue=2)
    checkbutton2.grid(row=3, column=0, padx=10, pady=5)

    # button implementation
    final_assign_button = tk.Button(final_assign, text="Assign", fg='blue')
    final_assign_button.grid(row=5, column=0, columnspan=2, pady=10)

view_booking()


