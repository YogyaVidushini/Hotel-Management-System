import tkinter as tk

def staff_reg():
    hotel_staff_reg=tk.Tk()
    hotel_staff_reg.title('Hotel Staff Registration')
    hotel_staff_reg.geometry('500x250')

    def on_button_click():
        name_in=entry_name.get()
        print("Name:", name_in)
        email_in=entry_email.get()
        print("Email:", email_in)
        phoneNo_in = entry_phoneNo.get()
        print("Phone Number:", phoneNo_in)
        pass_in = entry_password.get()
        print("Password:", pass_in)


    #Heading label
    label_top=tk.Label(hotel_staff_reg,text="Staff Registration", font=("Arial", 14))
    label_top.grid(row=0,column=0,columnspan=2, pady=10)

    #label_username and password
    name=tk.Label(hotel_staff_reg,text="  Name   : ").grid(row=1,column=0, padx=10, pady=5,sticky='e')
    email= tk.Label(hotel_staff_reg,text=" Email   : ").grid(row=2,column=0, padx=10, pady=5,sticky='e')
    phoneNo=tk.Label(hotel_staff_reg,text="Phone Number  : ").grid(row=3,column=0, padx=10, pady=5,sticky='e')
    password= tk.Label(hotel_staff_reg,text=" Password   : ").grid(row=4,column=0,padx=10, pady=5,sticky='e')

    #textboxes for username and password
    entry_name= tk.Entry(hotel_staff_reg)
    entry_name.grid(row=1,column=1 )
    entry_email= tk.Entry(hotel_staff_reg)
    entry_email.grid(row=2,column=1 )
    entry_phoneNo= tk.Entry(hotel_staff_reg)
    entry_phoneNo.grid(row=3,column=1 )
    entry_password= tk.Entry(hotel_staff_reg,show="*")
    entry_password.grid(row=4,column=1)

    #configure row and columns to expand
    hotel_staff_reg.grid_rowconfigure(0, weight=2)
    hotel_staff_reg.grid_rowconfigure(1, weight=1)
    hotel_staff_reg.grid_columnconfigure(0, weight=1)
    hotel_staff_reg.grid_columnconfigure(1, weight=1)


    #button implementation
    reg_button= tk.Button(hotel_staff_reg,text="Register",fg='blue', command=on_button_click)
    reg_button.grid(row=5, column=0, columnspan=2, pady=10)


    hotel_staff_reg.mainloop()
staff_reg()