from tkinter import *
import glob
import os


root = Tk()
root.geometry("400x400")
imgs = {}
for i in glob.glob("icons/*.png"):
	pathfile = i
	i = os.path.basename(i)
	name = i.split(".")[0]
	imgs[name] = PhotoImage(file=pathfile)


def callback():
    print("called the callback!")

# create a toolbar
toolbar = Frame(root)

b = Button(toolbar, relief=FLAT, compound = LEFT, text="new", command=callback, image=imgs["notepad"])
b.pack(side=LEFT, padx=0, pady=0)

b = Button(toolbar, text="open", compound = LEFT, command=callback, relief=FLAT, image=imgs["github"])
b.pack(side=LEFT, padx=0, pady=0)

toolbar.pack(side=TOP, fill=X)

mainloop()