import tkinter as tk

add_roomtype=tk.Tk()
add_roomtype.title('Add Room Type')
add_roomtype.geometry('500x250')
add_roomtype.configure(bg='lightblue')

def on_button_click():
    type_in=entry_room_type.get()
    print("Room Type:", type_in)


#Heading label
label_top=tk.Label(add_roomtype,text="ADD ROOM TYPE",bg='lightblue', font=("Times New Roman", 25, 'bold'))
label_top.grid(row=0,column=0,columnspan=2, pady=10)

#label_username and password
type= tk.Label(add_roomtype,text="Room Type: ",bg='lightblue',font=("Times New Roman", 15, 'bold')).grid(row=1,column=0, padx=10, pady=5,sticky='e')

#textboxes for username and password
entry_room_type= tk.Entry(add_roomtype,width=32)
entry_room_type.grid(row=1,column=1 )


#configure row and columns to expand
add_roomtype.grid_rowconfigure(0, weight=2)
add_roomtype.grid_rowconfigure(1, weight=1)
add_roomtype.grid_rowconfigure(2, weight=1)
add_roomtype.grid_rowconfigure(3, weight=1)
add_roomtype.grid_rowconfigure(4, weight=1)
add_roomtype.grid_columnconfigure(0, weight=1)
add_roomtype.grid_columnconfigure(1, weight=1)

#button implementation
add_button= tk.Button(add_roomtype,text="Add",fg='blue', command=on_button_click)
add_button.grid(row=3, column=0, columnspan=2, pady=10)


add_roomtype.mainloop()