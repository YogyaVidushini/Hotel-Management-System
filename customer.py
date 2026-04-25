import tkinter as tk
from tkinter import messagebox
def request_checkout():
    request_checkout=tk.Tk()
    request_checkout.title('Checkout')
    request_checkout.geometry('500x250')
    request_checkout.configure(bg='lightblue')

    #Heading label
    label_top=tk.Label(request_checkout,text="Checkout",bg='lightblue', font=("Times New Roman", 25, 'bold'))
    label_top.grid(row=0,column=0,columnspan=2, pady=10)

    #button implementation
    checkout_button= tk.Button(request_checkout,text="Request Checkout",fg='blue')
    checkout_button.grid(row=3, column=0, columnspan=2, pady=10)

    request_checkout.mainloop()
request_checkout()