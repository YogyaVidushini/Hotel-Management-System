import tkinter as tk
from tkinter import messagebox
def billing():
    billing=tk.Tk()
    billing.title('Admin Login')
    billing.geometry('500x250')
    billing.configure(bg='lightblue')

    #Heading label
    label_top=tk.Label(billing,text="Billing",bg='lightblue', font=("Times New Roman", 25, 'bold'))
    label_top.grid(row=0,column=0,columnspan=2, pady=10)

    #button implementation
    add_bills_button= tk.Button(billing,text="Add Bills",fg='blue',command= lambda: add_bill_amount(billing))
    add_bills_button.grid(row=3, column=0, columnspan=2, pady=10)

    billing.mainloop()

def add_bill_amount(billing):
    # Destroy the billing window when the add bill window opens
    billing.destroy()

    add_bill = tk.Toplevel()
    add_bill.title('Add Bill Amount')
    add_bill.geometry('500x250')

    # Heading label
    label_top = tk.Label(add_bill, text="Add Bill Amount", font=("Arial", 14))
    label_top.grid(row=0, column=0, columnspan=2, pady=10)

    #amount label
    amount = tk.Label(add_bill, text="  Amount(Rs.)   : ").grid(row=1, column=0, padx=10, pady=5, sticky='e')

    #textbox for amount
    entry_amount = tk.Entry(add_bill)
    entry_amount.grid(row=1, column=1)

    # button implementation
    request_payment_button = tk.Button(add_bill, text="Register", fg='blue')
    request_payment_button.grid(row=5, column=0, columnspan=2, pady=10)

billing()