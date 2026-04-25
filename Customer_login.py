import tkinter as tk
from tkinter import messagebox


def customer_login():
    customer_login=tk.Tk()
    customer_login.title('Customer Login')
    customer_login.geometry('500x250')
    customer_login.configure(bg='lightblue')


    def on_button_click():
        user_in=entry_email.get()
        print("Email:", user_in)
        pass_in=entry_password.get()
        print("Password:", pass_in)


    #Heading label
    label_top=tk.Label(customer_login,text="Customer Login",bg='lightblue', font=("Times New Roman", 25, 'bold'))
    label_top.grid(row=0,column=0,columnspan=2, pady=10)

    #label_username and password
    email= tk.Label(customer_login,text="Email: ",bg='lightblue',font=("Times New Roman", 15, 'bold')).grid(row=1,column=0, padx=10, pady=5,sticky='e')
    password= tk.Label(customer_login,text="Password: ",bg='lightblue',font=("Times New Roman", 15, 'bold')).grid(row=2,column=0,padx=10, pady=5,sticky='e')

    #textboxes for username and password
    entry_email= tk.Entry(customer_login)
    entry_email.grid(row=1,column=1 )
    entry_password= tk.Entry(customer_login,show="*")
    entry_password.grid(row=2,column=1)

    #configure row and columns to expand
    customer_login.grid_rowconfigure(0, weight=2)
    customer_login.grid_rowconfigure(1, weight=1)
    customer_login.grid_rowconfigure(2, weight=1)
    customer_login.grid_rowconfigure(3, weight=1)
    customer_login.grid_rowconfigure(4, weight=1)
    customer_login.grid_columnconfigure(0, weight=1)
    customer_login.grid_columnconfigure(1, weight=1)


    #No account link
    no_acc_label = tk.Label(customer_login, text="No Account?Register", fg='blue', bg='lightblue',font=("Times New Roman", 12, "underline"),cursor='hand')
    no_acc_label.grid(row=4, column=0,columnspan=2, pady=10)

    # Bind the click event to the label
    no_acc_label.bind("<Button-1>", lambda event: customer_reg())

    #button implementation
    login_button= tk.Button(customer_login,text="Login",fg='blue', command=on_button_click)
    login_button.grid(row=3, column=0, columnspan=2, pady=10)

"""customer registration"""

def customer_reg():
    cust_reg=tk.Toplevel()
    cust_reg.title('Customer Registration')
    cust_reg.geometry('500x250')

    def register():
        # Get inputs
        name_in = entry_name.get().strip()
        email_in = entry_email.get().strip()
        phoneNo_in = entry_phoneNo.get().strip()
        pass_in = entry_password.get().strip()

        # Validate inputs
        if not name_in or not email_in or not phoneNo_in or not pass_in:
            messagebox.showwarning("Warning", "Please fill out all fields.")
            return

        # Simulate saving the details
        print(f"Registered: {name_in}, {email_in}, {phoneNo_in}, {pass_in}")
        messagebox.showinfo("Success", "Registration Successful!")

        # Clear fields after successful registration
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_phoneNo.delete(0, tk.END)
        entry_password.delete(0, tk.END)

    #Heading label
    label_top=tk.Label(cust_reg,text="Customer Registration", font=("Arial", 14))
    label_top.grid(row=0,column=0,columnspan=2, pady=10)

    #label_username and password
    name=tk.Label(cust_reg,text="  Name   : ").grid(row=1,column=0, padx=10, pady=5,sticky='e')
    email= tk.Label(cust_reg,text=" Email   : ").grid(row=2,column=0, padx=10, pady=5,sticky='e')
    phoneNo=tk.Label(cust_reg,text="Phone Number  : ").grid(row=3,column=0, padx=10, pady=5,sticky='e')
    password= tk.Label(cust_reg,text=" Password   : ").grid(row=4,column=0,padx=10, pady=5,sticky='e')

    #textboxes for username and password
    entry_name= tk.Entry(cust_reg)
    entry_name.grid(row=1,column=1 )
    entry_email= tk.Entry(cust_reg)
    entry_email.grid(row=2,column=1 )
    entry_phoneNo= tk.Entry(cust_reg)
    entry_phoneNo.grid(row=3,column=1 )
    entry_password= tk.Entry(cust_reg,show="*")
    entry_password.grid(row=4,column=1)

    #configure row and columns to expand
    cust_reg.grid_rowconfigure(0, weight=2)
    cust_reg.grid_rowconfigure(1, weight=1)
    cust_reg.grid_columnconfigure(0, weight=1)
    cust_reg.grid_columnconfigure(1, weight=1)


    #button implementation
    reg_button= tk.Button(cust_reg,text="Register",fg='blue', command=register)
    reg_button.grid(row=5, column=0, columnspan=2, pady=10)


    cust_reg.mainloop()

    customer_login.mainloop()