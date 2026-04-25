import tkinter as tk

add_room=tk.Tk()
add_room.title('Add Rooms')
add_room.geometry('1500x800')
add_room.configure(bg='lightblue')

def on_button_click():
    # Fetch all the entry values
    room_type = entry_room_type.get()
    room_name = entry_room_name.get()
    room_size = entry_room_size.get()
    rooms_available = entry_rooms_available.get()
    room_price = entry_room_price.get()
    room_specialties = entry_room_specialties.get()
    room_image = entry_room_img.get()
    room_no = entry_room_no.get()
    room_about = entry_room_about.get()

    # Print them to console for now
    print("Room Type:", room_type)
    print("Room Name:", room_name)
    print("Room Size:", room_size)
    print("Rooms Available:", rooms_available)
    print("Price Per Day:", room_price)
    print("Specialties:", room_specialties)
    print("Image:", room_image)
    print("Room Number:", room_no)
    print("About:", room_about)

def browse_file():
    # Open a file dialog and get the selected file path
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp"), ("All Files", "*.*")]
    )
    # Insert the file path into the "Room Image" entry
    entry_room_img.delete(0, tk.END)  # Clear any existing text
    entry_room_img.insert(0, file_path)



label_top = tk.Label(add_room, text="ADD ROOMS", bg='lightblue', font=("Times New Roman", 25, 'bold'))
label_top.grid(row=0, column=1, pady=10, sticky='n')

# Labels
type = tk.Label(add_room, text="Room Type: ", bg='lightblue', font=("Times New Roman", 15, 'bold')).grid(row=1, column=0, padx=10, sticky='e')
name = tk.Label(add_room, text="Room Name: ", bg='lightblue', font=("Times New Roman", 15, 'bold')).grid(row=1, column=1, padx=20, pady=10, sticky='e')
size = tk.Label(add_room, text="Room Size: ", bg='lightblue', font=("Times New Roman", 15, 'bold')).grid(row=2, column=0, padx=10, pady=5, sticky='e')
available_rooms = tk.Label(add_room, text="No.of Rooms Available: ", bg='lightblue', font=("Times New Roman", 15, 'bold')).grid(row=2, column=1, padx=10, pady=5, sticky='e')
price = tk.Label(add_room, text="Price Per Day: ", bg='lightblue', font=("Times New Roman", 15, 'bold')).grid(row=3, column=0, padx=10, pady=5, sticky='e')
specialties = tk.Label(add_room, text="Room Specialties: ", bg='lightblue', font=("Times New Roman", 15, 'bold')).grid(row=3, column=1, padx=10, pady=5, sticky='e')
room_image = tk.Label(add_room, text="Room Image: ", bg='lightblue', font=("Times New Roman", 15, 'bold')).grid(row=4, column=0, padx=10, pady=5, sticky='e')
room_no = tk.Label(add_room, text="Room Number: ", bg='lightblue', font=("Times New Roman", 15, 'bold')).grid(row=4, column=1, padx=10, pady=5, sticky='e')
about = tk.Label(add_room, text="About: ", bg='lightblue', font=("Times New Roman", 15, 'bold')).grid(row=5, column=0, padx=10, pady=5, sticky='e')

# Textboxes for inputs
entry_room_type = tk.Entry(add_room, width=32)
entry_room_type.grid(row=1, column=1, sticky='w')
entry_room_name = tk.Entry(add_room, width=32)
entry_room_name.grid(row=1, column=2, sticky='w')
entry_room_size = tk.Entry(add_room, width=32)
entry_room_size.grid(row=2, column=1, sticky='w')
entry_rooms_available = tk.Entry(add_room, width=32)
entry_rooms_available.grid(row=2, column=2, sticky='w')
entry_room_price = tk.Entry(add_room, width=32)
entry_room_price.grid(row=3, column=1, sticky='w')
entry_room_specialties = tk.Entry(add_room, width=32)
entry_room_specialties.grid(row=3, column=2, sticky='w')
entry_room_img = tk.Entry(add_room, width=32)
entry_room_img.grid(row=4, column=1, sticky='w')
entry_room_no = tk.Entry(add_room, width=32)
entry_room_no.grid(row=4, column=2, sticky='w')
entry_room_about = tk.Entry(add_room, width=50)
entry_room_about.grid(row=5, column=1, sticky='w')

# File Browser Button for "Room Image"
browse_button = tk.Button(add_room, text="Browse", command=browse_file)
browse_button.grid(row=4, column=2, sticky='w')

# Configure rows for expandability
add_room.grid_rowconfigure(0, weight=2)
add_room.grid_rowconfigure(1, weight=1)
add_room.grid_rowconfigure(2, weight=1)
add_room.grid_rowconfigure(3, weight=1)
add_room.grid_rowconfigure(4, weight=1)
add_room.grid_rowconfigure(5, weight=1)
add_room.grid_rowconfigure(6, weight=1)
add_room.grid_rowconfigure(7, weight=1)
add_room.grid_rowconfigure(8, weight=1)

# Configure columns for better responsiveness
add_room.grid_columnconfigure(0, weight=1)
add_room.grid_columnconfigure(1, weight=1)
add_room.grid_columnconfigure(2, weight=1)

# Button to trigger action
add_button = tk.Button(add_room, text="Add", fg='blue', width=5, command=on_button_click)
add_button.grid(row=6, column=1, pady=10, sticky='e')

add_room.mainloop()
