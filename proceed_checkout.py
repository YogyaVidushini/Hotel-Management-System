import tkinter as tk
from tkinter import messagebox
def proceed_checkout():
    proceed_checkout=tk.Tk()
    proceed_checkout.title('Admin Login')
    proceed_checkout.geometry('500x250')
    proceed_checkout.configure(bg='lightblue')

    #Heading label
    label_top=tk.Label(proceed_checkout,text="Billing",bg='lightblue', font=("Times New Roman", 25, 'bold'))
    label_top.grid(row=0,column=0,columnspan=2, pady=10)

    #button implementation
    checkout_button= tk.Button(proceed_checkout,text="Proceed Checkout",fg='blue')
    checkout_button.grid(row=3, column=0, columnspan=2, pady=10)

    proceed_checkout.mainloop()
proceed_checkout()