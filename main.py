# main.py
import tkinter as tk
import os


linkslist = {
"Open file dialog button": "https://pythonprogramming.altervista.org/tkinter-templates-chapter-1-open-file-dialog/",
"Entry and Text": "https://pythonprogramming.altervista.org/tkinter-templates-part-2-window-with-an-entry-and-a-text-area-widget/"
}

	
def generate_link_list():
	with open("links.html", "w") as file:
		for title, link in linkslist.items():
			print(f"<a href='{link}'>{title}</a><br>", file=file)
	os.system("links.html")


root = tk.Tk()

but = tk.Button(root,
	text="Generate link list",
	command=generate_link_list)
but.pack()

root.mainloop()