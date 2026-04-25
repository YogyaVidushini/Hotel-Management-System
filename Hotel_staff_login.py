import tkinter as tk
from Staff_dashboard import staff_dash
from tkinter import messagebox


def staff_login():
    hotel_staff_login=tk.Tk()
    hotel_staff_login.title('Hotel Staff Login')
    hotel_staff_login.geometry('500x250')
    hotel_staff_login.configure(bg='lightblue')

    #Heading label
    label_top=tk.Label(hotel_staff_login,text="Hotel Staff Login", bg='lightblue', font=("Times New Roman", 25, 'bold'))
    label_top.grid(row=0,column=0,columnspan=2, pady=10)

    #label_username and password
    email= tk.Label(hotel_staff_login,text="Email: ",bg='lightblue', font=("Times New Roman", 15, 'bold')).grid(row=1,column=0, padx=10, pady=5,sticky='e')
    password= tk.Label(hotel_staff_login,text="Password: ",bg='lightblue', font=("Times New Roman", 15, 'bold')).grid(row=2,column=0,padx=10, pady=5,sticky='e')

    #textboxes for username and password
    entry_email= tk.Entry(hotel_staff_login)
    entry_email.grid(row=1,column=1 )
    entry_password= tk.Entry(hotel_staff_login,show="*")
    entry_password.grid(row=2,column=1)

    #configure row and columns to expand
    hotel_staff_login.grid_rowconfigure(0, weight=1)
    hotel_staff_login.grid_rowconfigure(1, weight=1)
    hotel_staff_login.grid_columnconfigure(0, weight=1)
    hotel_staff_login.grid_columnconfigure(1, weight=1)

    # Define the login button functionality
    def on_login():
        user_email = entry_email.get().strip()
        user_password = entry_password.get().strip()

        if not user_email or not user_password:
            messagebox.showwarning("Warning", "Please fill out all fields.")
            return

        # Simulate login validation
        if user_email == "staff@example.com" and user_password == "staff123":
            messagebox.showinfo("Login Successful", "Welcome, Staff!")
            hotel_staff_login.destroy()  # Close the login window
            staff_dash()  # Open the staff dashboard
        else:
            messagebox.showerror("Login Failed", "Invalid email or password.")


    #button implementation
    login_button= tk.Button(hotel_staff_login,text="Login",fg='blue', command=staff_dash)
    login_button.grid(row=3, column=0, columnspan=2, pady=10)


    hotel_staff_login.mainloop()