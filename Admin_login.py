import tkinter as tk
import Admin_dashboard
from tkinter import messagebox


def admin_login():
    login=tk.Tk()
    login.title('Admin Login')
    login.geometry('500x250')
    login.configure(bg='lightblue')

    def on_login():
        email_in = entry_email.get().strip()
        password_in = entry_password.get().strip()

        if not email_in or not password_in:
            messagebox.showwarning("Warning", "Please fill out all fields.")
            return

        # Simulate login validation
        if email_in == "yogya@gmail.com" and password_in == "admin123":
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
            login.destroy()  # Close the login window
            Admin_dashboard.admin_dash()  # Open the admin dashboard
        else:
            messagebox.showerror("Login Failed", "Invalid email or password.")

    #Heading label
    label_top=tk.Label(login,text="Login",bg='lightblue', font=("Times New Roman", 25, 'bold'))
    label_top.grid(row=0,column=0,columnspan=2, pady=10)

    #label_username and password
    email= tk.Label(login,text="Email: ",fg='black',bg='lightblue',font=("Times New Roman", 15, 'bold')).grid(row=1,column=0, padx=10, pady=5,sticky='e')
    password= tk.Label(login,text="Password: ",fg='black',bg='lightblue',font=("Times New Roman", 15, 'bold')).grid(row=2,column=0,padx=10, pady=5,sticky='e')

    #textboxes for username and password
    entry_email= tk.Entry(login)
    entry_email.grid(row=1,column=1 )
    entry_password= tk.Entry(login,show="*")
    entry_password.grid(row=2,column=1)

    #configure row and columns to expand
    login.grid_rowconfigure(0, weight=2)
    login.grid_rowconfigure(1, weight=1)
    login.grid_rowconfigure(2, weight=1)
    login.grid_columnconfigure(0, weight=1)
    login.grid_columnconfigure(1, weight=1)


    # Clear fields after successful registration
    entry_email.delete(0, tk.END)
    entry_password.delete(0, tk.END)

    #button implementation
    login_button= tk.Button(login,text="Login",fg='blue', command=on_login)
    login_button.grid(row=3, column=0, columnspan=2, pady=10)


    login.mainloop()