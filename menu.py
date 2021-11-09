import tkinter as tk

root = tk.Tk()
w = root.winfo_height
root.geometry("400x400+500+400")

lab1 = tk.Label(root,
	text="Hello",
	font="Arial 20",
	bg="yellow")
lab1.pack()

menu = tk.Menu()
menu.add_command(label="Refresh", command=None)
root.configure(menu=menu)

root.mainloop()