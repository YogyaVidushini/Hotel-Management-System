import tkinter as tk

#admin_login():
change_pas=tk.Tk()
change_pas.title('Reset Password')
change_pas.geometry('500x250')
change_pas.configure(bg='lightblue')

#Heading label
label_top=tk.Label(change_pas,text="Reset Password",bg='lightblue', font=("Times New Roman", 25, 'bold'))
label_top.grid(row=0,column=0,columnspan=2, pady=10)

old_password = tk.Label(change_pas, text="Old Password: ", fg='black', bg='lightblue', font=("Times New Roman", 15, 'bold')).grid(row=1,column=0,padx=10,pady=5,sticky='e')
new_password = tk.Label(change_pas, text="New Password: ", fg='black', bg='lightblue', font=("Times New Roman", 15, 'bold')).grid(row=2, column=0, padx=10, pady=5, sticky='e')
repeat_password = tk.Label(change_pas, text="Repeat Password: ", fg='black', bg='lightblue', font=("Times New Roman", 15, 'bold')).grid(row=3, column=0, padx=10, pady=5, sticky='e')

entry_old= tk.Entry(change_pas,show="*")
entry_old.grid(row=1,column=1 )
entry_new= tk.Entry(change_pas,show="*")
entry_new.grid(row=2,column=1)
entry_repeat= tk.Entry(change_pas,show="*")
entry_repeat.grid(row=3,column=1 )

#configure row and columns to expand
change_pas.grid_rowconfigure(0, weight=2)
change_pas.grid_rowconfigure(1, weight=1)
change_pas.grid_rowconfigure(2, weight=1)
change_pas.grid_columnconfigure(0, weight=1)
change_pas.grid_columnconfigure(1, weight=1)

change_button= tk.Button(change_pas,text="Change",fg='blue')
change_button.grid(row=4, column=0, columnspan=2, pady=10)

change_pas.mainloop()

