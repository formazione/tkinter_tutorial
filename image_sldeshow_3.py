import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageBrowser:
    def __init__(self, root):
        # Create a frame to hold the image and buttons
        self.frame = tk.Frame(root)
        self.frame.pack()

        # Create the "Open" button
        self.open_button = tk.Button(self.frame, text="Open", command=self.open_image)
        self.open_button.pack(side="left")

        # Create the "Previous" button
        self.prev_button = tk.Button(self.frame, text="Previous", command=self.show_prev_image)
        self.prev_button.pack(side="left")

        # Create the "Next" button
        self.next_button = tk.Button(self.frame, text="Next", command=self.show_next_image)
        self.next_button.pack(side="left")

        # Create the label to display the image
        self.label = tk.Label(root)
        self.label.pack()

        # Set the initial image index
        self.current_image = 0
        self.image_files = []

    def open_image(self):
        # Open a file dialog and get the selected file(s)
        file_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg;*.png;*.gif")])

        # If a file was selected, update the image list and display the first image
        if file_paths:
            self.image_files = file_paths
            self.current_image = 0
            self.show_image()

    def show_prev_image(self):
        # Decrement the image index and display the previous image
        self.current_image -= 1
        self.show_image()

    def show_next_image(self):
        # Increment the image index and display the next image
        self.current_image += 1
        self.show_image()

    def show_image(self):
        # Check if the index is within the range of the image list
        if self.current_image >= 0 and self.current_image < len(self.image_files):
            # Load the image from the file and display it in the label
            image = Image.open(self.image_files[self.current_image])
            image = image.resize((400, 400), Image.ANTIALIAS)
            image = ImageTk.PhotoImage(image)
            self.label.config(image=image)
            self.label.image = image

# Create the root window
root = tk.Tk()

# Create the image browser and start the main loop
app = ImageBrowser(root)
root.mainloop()
