import tkinter as tk
from tkinter import messagebox
import pdfkit
import os
import codecs

# pip install pdfkit
# this will install wkhtmltopdf
path_wkhtmltopdf = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
# pdfkit.from_url("http://google.com", "out.pdf", configuration=config)

class Window():
    def __init__(self):
        self.root = tk.Tk()
        self.widgets()
        self.root.mainloop()

    def widgets(self):
        self.menubar = tk.Menu(self.root)
        self.menubar.add_command(label="PDF from String", command=self.from_string)
        self.menubar.add_command(label="PDF from URL", command=self.from_url)
        self.menubar.add_command(label="Open pdf", command=self.open)
        self.menubar.add_command(label="Help", command=self.help)
        self.root.config(menu=self.menubar)
        self.label = tk.Label(self.root, text="SCRIPT GENTLY OFFERED BY @PYTHONPROGRAMMI AKA GIOVANNIPYTHON")
        self.label.pack()
        self.txbx = tk.Text(self.root, height=20, insertbackground="white")
        self.txbx['font'] = "Arial 14"
        self.txbx['bg'] = "black"
        self.txbx['fg'] = "white"
        self.txbx['borderwidth'] = 2
        self.txbx.pack(fill=tk.BOTH, expand=1)
        self.txbx.focus()
        self.txbx.bind("<Control-s>", self.from_string)
        self.txbx.bind("<Control-o>", self.open)

    def open(self, event=""):
        os.startfile("pdf2.pdf")

    def help(self, event=""):
        messagebox.showinfo("HELP", "Scrivi qualcosa usando anche l'HTML\nCTRL + s per salvare il file\CTRL + o per aprirlo nel beowser")

    def from_file(self):
        with open("pdf.html", "w") as file:
            file.write(content)
        pdfkit.from_file("pdf.html", "pdf2.pdf", configuration=config)

    def from_url(self):
        self.get_content()
        pdfkit.from_url(self.content, "pdf2.pdf", configuration=config)

    def get_content(self):
        self.content = self.txbx.get("0.0", tk.END)
        self.content = self.content.replace("\n", "<br>")

    def from_string(self, event=""):
        self.get_content()
        pdfkit.from_string(self.content, "pdf2.pdf", configuration=config)
        print("Salvato file pdf (ctrl+o per vederlo)")
        messagebox.showinfo("File creato","CTRL + o per aprire il file")



win = Window()