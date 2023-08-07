import tkinter as tk
from tkinter import PhotoImage

def window(image):
    # Create the main window
    window = tk.Tk()

    # Load the image using the PhotoImage class
    image = PhotoImage(file=image)

    # Create a label to display the image
    label = tk.Label(window, image=image)

    # Pack the label to display it in the window
    label.pack()

    # Run the tkinter event loop
    window.mainloop()



window("001.png")