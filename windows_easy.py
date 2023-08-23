import tkinter as tk


root = tk.Tk()
root.geometry("400x400")
root.title("MAIN")
text = tk.Text(root,
	font="Arial 26")
text.pack()

tl1 = tk.Toplevel(root)
tl1.title("TL1")
tl1.but1 = tk.Button(tl1,
	text="Click LT1 BT1",
	command=lambda: text.insert(tk.END, f"You clicked BT1 {tl1.but1['text']}"))

tl1.but1.pack()

tl2 = tk.Toplevel(root)
tl2.title("TL2")



root.mainloop()