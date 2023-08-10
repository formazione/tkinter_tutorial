import tkinter as tk
from tkinter import PhotoImage
from glob import glob


class Window:
    
    def __init__(self, images: list):
        self.images = images
        self.imagepos = 0
        self.root = tk.Tk()
        self.widgets()
        self.root.mainloop()

    def widgets(self):
        self.lab_image()
        self.start_slide_button()

    def lab_image(self):
        self.img = PhotoImage(file=self.images[self.imagepos])
        self.label = tk.Label(self.root, image=self.img)
        self.label.pack()



    def start_slide_button(self):
        self.butstart = tk.Button(self.root,
            text="Start slideshow",
            command=self.slideshow)
        self.butstart.pack()

    def slideshow(self):
        if self.imagepos < len(self.images) - 1:
            self.imagepos += 1
        else:
            self.imagepos = 0
        self.img = PhotoImage(file=self.images[self.imagepos])
        self.label["image"] = self.img


images = glob("images\\*png")
win = Window(images)