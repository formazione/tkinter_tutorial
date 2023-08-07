import tkinter as tk

def on_button_click():
    text = entry.get()
    text_widget.insert(tk.END, f"Text entered: {text}\n")
    entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Tkinter Window")

# Entry widget
entry = tk.Entry(window, width=30)
entry.pack(pady=10)

# Text widget
text_widget = tk.Text(window, width=30, height=10)
text_widget.pack()

# Button widget
button = tk.Button(window, text="Submit", command=on_button_click)
button.pack(pady=10)

# Start the main event loop
window.mainloop()