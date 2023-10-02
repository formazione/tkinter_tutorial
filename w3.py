import tkinter as tk


root = tk.Tk()

toplev1 = tk.Toplevel(root)
toplev1.geometry("400x100")
but = tk.Button(toplev1,
	text="Click me to title me toplevel1",
	command=lambda: toplev1.title("Toplev1"))
but.pack()


root.mainloop()