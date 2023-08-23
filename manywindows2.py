# tkinter Toplevel windows with class
# GiovanniPython on YT
# @pythonprogrammi on X

import tkinter as tk

bdict = {}
class Top:
	def __init__(self, size="400x400"):
		self.root = tk.Toplevel(root)
		self.root.geometry(size)

	def title(self, name):
		self.root.title(name)

	def button(self, name, text) -> tk.Button:
		b = tk.Button(self.root,
			text=text)
		b.pack()
		bdict[name] = b
		return b

	def add_command(self, name, command):
		bdict[name]["command"] = command



def toplevel1():
	x = Top()
	x.title("Top 1")
	# the first parameter is the name of the button
	x.button("bx1", "Click me I am bx1")
	# it's important to add the command to the right button
	x.add_command("bx1", lambda: print("Bx1"))
	x.button("bx2", "Click me I am bx2")
	x.add_command("bx2", lambda: print("Bx2"))

def toplevel2():
	y = Top()
	y.title("Top 2")
	y.button("by1", "Click me I am by1")
	y.add_command("by1", lambda: print("By1"))


def main_window():
	global root

	root = tk.Tk()
	root.title("Main")
	toplevel1()
	toplevel2()
	root.mainloop()

main_window()