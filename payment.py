import tkinter as tk


pay=tk.Tk()
pay.title('Payment')
pay.geometry('500x500')
pay.configure(bg='lightblue')

#Heading label
label_top=tk.Label(pay,text="Payment",bg='lightblue', font=("Times New Roman", 25, 'bold'))
label_top.grid(row=0,column=0,columnspan=2, pady=10)

card_type = tk.Label(pay, text="Card Type: ", fg='black', bg='lightblue', font=("Times New Roman", 15, 'bold')).grid(row=1,column=0,padx=10,pady=5,sticky='e')
name_card = tk.Label(pay, text="Name on Card: ", fg='black', bg='lightblue', font=("Times New Roman", 15, 'bold')).grid(row=2, column=0, padx=10, pady=5, sticky='e')
card_no = tk.Label(pay, text="Card Number: ", fg='black', bg='lightblue', font=("Times New Roman", 15, 'bold')).grid(row=3, column=0, padx=10, pady=5, sticky='e')
cvv = tk.Label(pay, text="CVV: ", fg='black', bg='lightblue', font=("Times New Roman", 15, 'bold')).grid(row=4, column=0, padx=10, pady=5, sticky='e')
amount = tk.Label(pay, text="Amount(Rs.): ", fg='black', bg='lightblue', font=("Times New Roman", 15, 'bold')).grid(row=5, column=0, padx=10, pady=5, sticky='e')
expiry = tk.Label(pay, text="Expire: ", fg='black', bg='lightblue', font=("Times New Roman", 15, 'bold')).grid(row=6, column=0, padx=10, pady=5, sticky='e')

entry_type= tk.Entry(pay)
entry_type.grid(row=1,column=1 )
entry_name= tk.Entry(pay)
entry_name.grid(row=2,column=1)
entry_card_no= tk.Entry(pay)
entry_card_no.grid(row=3,column=1 )
entry_cvv= tk.Entry(pay)
entry_cvv.grid(row=4,column=1 )
entry_amount= tk.Entry(pay)
entry_amount.grid(row=5,column=1 )
entry_expiry= tk.Entry(pay)
entry_expiry.grid(row=6,column=1 )

#configure row and columns to expand
pay.grid_rowconfigure(0, weight=2)
pay.grid_rowconfigure(1, weight=1)
pay.grid_rowconfigure(2, weight=1)
pay.grid_rowconfigure(3, weight=1)
pay.grid_rowconfigure(4, weight=1)
pay.grid_rowconfigure(5, weight=1)
pay.grid_rowconfigure(6, weight=1)
pay.grid_columnconfigure(0, weight=1)
pay.grid_columnconfigure(1, weight=1)

pay_button= tk.Button(pay,text="Pay",fg='blue')
pay_button.grid(row=7, column=0, columnspan=2, pady=10)

pay.mainloop()

