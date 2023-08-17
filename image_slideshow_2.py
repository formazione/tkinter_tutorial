import tkinter as tk
from tkinter import PhotoImage
from glob import glob

cnt_img = 0

def next_image(event):
    global cnt_img, images, label
    if event.keysym=="Right":
        if cnt_img < len(images) - 1:
            cnt_img += 1
    if event.keysym=="Left":
        if cnt_img > 0:
            cnt_img -= 1
    
    show_image(cnt_img)


def show_image(cntimg):
    print(cntimg)
    img = images[cntimg]
    label["image"]=images[cntimg]
    label.pack()


def window():
    global cnt_img, images, label
    # Create the main window
    window = tk.Tk()

    images = [tk.PhotoImage(file=image) for image in glob("images/*.png")]
    print(images)
    # Load the image using the PhotoImage class
    # image = PhotoImage(file=image)
    img = images[cnt_img]
    # Create a label to display the image
    label = tk.Label(window, image=images[cnt_img])

    # Pack the label to display it in the window
    label.pack()
    window.bind("<Right>", next_image)
    window.bind("<Left>", next_image)
    print("Im here")
    window.mainloop()


window()