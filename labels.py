import tkinter as tk

root = tk.Tk()
print(dir(tk))
root.geometry("400x400+500+400")

lab1 = tk.Label(root,
	text="Hello",
	font="Arial 20",
	bg="yellow")
lab1.pack()


root.mainloop()