import tkinter as tk
from tkinter import ttk
from generator import *


def GUI():
    # Create the main window
    root = tk.Tk()
    root.title("Random Password Generator")

    # Create a frame to hold the widgets side by side
    frame = tk.Frame(root)
    frame.pack(pady=10, padx=10)

    # Create a Combobox widget (dropdown list)
    options = [i for i in range(5, 21)]  # 15 options from 5 to 20
    combobox = ttk.Combobox(frame, values=options, width=20)
    combobox.grid(row=0, column=1, padx=5)
    combobox.set("5")  # Set a default placeholder text

    # Create an Entry widget (text field)
    readonly_entry = tk.Entry(frame, width=23)
    readonly_entry.grid(row=0, column=0, padx=5, pady=5)  # Adjusted grid placement
    readonly_entry.insert(0, "Number of Password Characters")
    readonly_entry.config(state='readonly')

    # Create an Entry widget (text field)
    e1 = tk.Entry(frame, width=23)
    e1.grid(row=1, column=0, padx=5, pady=5)  # Adjusted grid placement
    e1.insert(0, "Password:")
    e1.config(state='readonly')

    password_entry = tk.Entry(frame, width = 20)
    password_entry.grid(row=1, column=1, padx=5, pady=5)  # Adjusted grid placement
    password_entry.config(state='readonly')

    # Define a function to handle the button click event
    def on_button_click():
        password = generator(int(combobox.get()))
        # Update the existing Entry widget with the generated password
        password_entry.config(state='normal')  # Set state to normal to allow modification
        password_entry.delete(0, tk.END)  # Clear previous content
        password_entry.insert(0, password)  # Insert the generated password
        password_entry.config(state='readonly')  # Set state back to readonly

    # Create a Button widget
    button = tk.Button(root, text="Generate", command=on_button_click)
    button.pack(pady=10)

    root.mainloop()


if __name__ == '__main__':
    GUI()
