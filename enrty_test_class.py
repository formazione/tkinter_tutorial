# entry_test_class.py
# template with entry and text, the text in the entry is passed in the text area


import tkinter as tk


# Create the main window
class Window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tkinter Window")

        # Entry widget
        self.entry = tk.Entry(self.window, width=30)
        self.entry.pack(pady=10)

        # Text widget
        self.text_widget = tk.Text(self.window, width=30, height=10)
        self.text_widget.pack()

        # Button widget
        self.button = tk.Button(self.window, 
            text="Submit", 
            command=self.on_button_click)
        self.button.pack(pady=10)
        self.window.mainloop()

    def on_button_click(self):
        self.text = self.entry.get()
        self.text_widget.insert(tk.END, f"Text entered: {self.text}\n")
        self.entry.delete(0, tk.END)

win = Window()