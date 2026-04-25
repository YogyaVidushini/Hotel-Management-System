import tkinter as tk
import Admin_login
from Hotel_staff_login import staff_login
from Customer_login import customer_login

def main():

    home=tk.Tk()
    home.title('Homepage')
    home.geometry('750x500')
    home.configure(bg='lightblue')

    main_label=tk.Label(home, text="HOTEL MANAGEMENT SYSTEM",fg='White', bg="black", font=("Times New Roman", 30, "bold"),height=4)
    main_label.pack(pady=10, fill="x")

    button_frame = tk.Frame(home,bg='lightblue',padx=10, pady=10, height=6)
    button_frame.pack(pady=20)


    admin_button= tk.Button(button_frame,text="ADMIN",command=Admin_login.admin_login,width=15)
    admin_button.grid(row=0, column=0, padx=5, pady=5)

    staff_button= tk.Button(button_frame,text="HOTEL STAFF",command=staff_login,width=15)
    staff_button.grid(row=0, column=1,padx=5, pady=5)

    customer_button= tk.Button(button_frame,text="CUSTOMER",command=customer_login,width=15)
    customer_button.grid(row=0, column=2, padx=5, pady=5)

    #configure row and columns to expand
    home.grid_rowconfigure(0, weight=2)
    home.grid_columnconfigure(0, weight=2)
    home.grid_columnconfigure(1, weight=2)
    home.grid_columnconfigure(2, weight=2)


    wel_label=tk.Label(home,text="WELCOME",fg='blue',bg='grey', font=("Times New Roman", 60,"bold"))
    wel_label.pack(pady=5)

    home.mainloop()

main()
