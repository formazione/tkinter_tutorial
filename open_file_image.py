import tkinter as tk
from tkinter import filedialog


class Win:
    "Show images passed as argument"
    
    def __init__(self, imagepath):
        self.img = tk.PhotoImage(file=imagepath)
        self.add_label()
        self.add_button()

    def add_label(self):
        self.label = tk.Label(root,
            image = self.img)
        self.label.pack()
        # self.image = img # WITHOUT THIS YOU WILL SEE NO IMAGE

    def add_button(self):
        self.button = tk.Button(
            root,
            text="Open file",
            command=self.openf)
        self.button.pack()

    def openf(self):
        self.file_path = filedialog.askopenfilename()
        self.img = tk.PhotoImage(file=self.file_path)
        # image = Image.open(file_path)
        self.label["image"] = self.img
        self.image = self.img # WITHOUT THIS YOU WILL SEE NO IMAGE


root = tk.Tk()
root.geometry("400x400+500+500")
im = Win("")

root.mainloop()