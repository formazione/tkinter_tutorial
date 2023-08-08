# dialog.py
# opens filedialog with a button, then write file chosen name in label

import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        label.config(text=f"Selected file: {file_path}")

# Create the main window
window = tk.Tk()
window.title("File Dialog Example")

# Button to open file dialog
button = tk.Button(window, text="Open File", command=open_file_dialog)
button.pack(pady=10)

# Label to display the selected file name
label = tk.Label(window, text="Selected file: ")
label.pack()

# Start the main event loop
window.mainloop()
