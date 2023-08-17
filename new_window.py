# I was asked to make 3 pop up window at start, so I made this script
# you can find the video tutorial here:
# the repository is here: https://github.com/formazione/tkinter_tutorial.git
# GiovanniPython on YT
# @pythonprogrammi on X


import tkinter as tk


def new_win(name,
		labeltext="",
		font="Arial 20"):
	x = tk.Toplevel(root)
	x.title(name)
	x.label = tk.Label(x,
		font=font,
		text=labeltext)
	x.label.pack()
	return x


root = tk.Tk()
root.title("MAIN WINDOW")
x = new_win("POP 1",
	"If you have questions or something to ask, write it in the comments")
print(x)
y = new_win("POP 2",
	"That's all")
print(y)
z = new_win("POP 3",
	"Bye remember to subscribe, so you do not lose anything")
print(z)

root.mainloop()