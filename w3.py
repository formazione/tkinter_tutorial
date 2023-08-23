import tkinter as tk


root = tk.Tk()

toplev1 = tk.Toplevel(root)
but = tk.Button(toplev1,
	text="Click me i'm on toplevel1",
	command=lambda: toplev1.title("Toplev1"))
but.pack()
toplev2 = tk.Toplevel(root)
toplev3 = tk.Toplevel(root)
toplev4 = tk.Toplevel(root)
toplev5 = tk.Toplevel(root)

root.mainloop()