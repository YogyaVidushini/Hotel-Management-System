import tkinter as tk
import main_dashboard
import Admin_login

def admin_dash():
    admin_dash=tk.Tk()
    admin_dash.title('ADMIN')
    admin_dash.geometry('1000x1000')
    admin_dash.configure(bg='#F1BF41')

    main_label=tk.Label(admin_dash, text="ADMIN",fg='black', bg="grey", font=("Times New Roman", 30, "bold"),height=1)
    main_label.grid(row=0,column=0,padx=10, pady=10)

    log_out= tk.Button(admin_dash,text="LOG OUT",bg='red',fg='red',font=('Times New Roman',15,"bold"), width=15,command=main_dashboard.main())
    log_out.grid(row=0, column=4, padx=5, pady=5, sticky ='e')

    button_frame = tk.Frame(admin_dash,bg='grey',padx=10, pady=10, height=6)
    button_frame.grid(row=1, column=0, columnspan=5, pady=20)



    add_staff= tk.Button(button_frame,text="Add hotel staff",width=15)
    add_staff.grid(row=1, column=0, padx=5, pady=5)

    view_staff= tk.Button(button_frame,text="View hotel staff",width=15)
    view_staff.grid(row=1, column=1,padx=5, pady=5)

    add_view_roomType= tk.Button(button_frame,text="Add/View Room Type",width=15)
    add_view_roomType.grid(row=1, column=2, padx=5, pady=5)

    add_room= tk.Button(button_frame,text="Add Rooms",width=15)
    add_room.grid(row=1, column=3, padx=5, pady=5)

    view_room= tk.Button(button_frame,text="View Rooms",width=15)
    view_room.grid(row=1, column=4, padx=5, pady=5)

    #configure row and columns to expand
    admin_dash.grid_rowconfigure(0, weight=2)
    admin_dash.grid_rowconfigure(1, weight=2)
    admin_dash.grid_rowconfigure(2, weight=2)
    admin_dash.grid_columnconfigure(1, weight=2)
    admin_dash.grid_columnconfigure(2, weight=2)
    admin_dash.grid_columnconfigure(3, weight=2)
    admin_dash.grid_columnconfigure(4, weight=2)

    wel_label=tk.Label(admin_dash,text="WELCOME ADMIN",fg='white',bg='grey', font=("Times New Roman", 60,"bold"),height=5)
    wel_label.grid(row=2, columnspan=5, pady=10, sticky='ew')


    admin_dash.mainloop()
