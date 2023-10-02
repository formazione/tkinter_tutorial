import tkinter as tk


def tl1_onclick():
	toplev1.title("Toplev1")


root = tk.Tk()
tl1 = tk.Toplevel(root)
tl1.geometry("400x100+300+100")
but = tk.Button(tl1,
	text="Click me to title me toplevel1",
	command=lambda: tl1_conclick)
but.pack()


root.mainloop()