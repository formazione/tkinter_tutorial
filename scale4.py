import tkinter as tk
from random import randint

def get_csv(csv_filename: str) -> list:
	''' return a list with an item for each line of the file '''
	with open(csv_filename) as file:
		itemslist = file.readlines()
	return itemslist


def create_dic(content):
	coldic = {}
	for k in content:
		id,name,hx,r,g,b = k.split(",")
		name = name.replace("\"","")
		b = b.replace("\n","")
		coldic[f"{r},{g},{b}"] = name
	return coldic

coldic = create_dic(get_csv("colors.csv"))


# ====== TKINTER GUI ===========
class Window:

	def __init__(self):
		self.root = tk.Tk()
		self.root.geometry("800x600")
		self.root.title("Colorpicker - pythonprogramming.altervista.org - YT GiovanniPython - X @pythonprogrammi")
		self.root.config(background="black")


	def loop(self):
		self.create_widgets()
		self.root.mainloop()


	def create_widgets(self):
		self.label_color_hex()
		self.color1 = 0
		self.color2 = 0
		self.color3 = 0


	def label_color_hex(self):
		# NAME =========================
		self.clrtext = tk.Label(self.root,
			text="Name",
			font="Arial 20",
			)
		self.clrtext.pack(pady=0)
		self.name = tk.StringVar()
		self.colorname = tk.Entry(self.root,
			textvariable=self.name,
			font="Arial 20",
			)
		self.colorname.pack(pady=0)

		# HEX ===========================
		self.hexlab = tk.Label(self.root,
			text="Hexadecimal",
			font="Arial 20",
			)
		self.hexlab.pack(pady=0)
		self.x = tk.IntVar()
		self.label = tk.Entry(self.root,
			textvariable=self.x,
			font="Arial 20",
			)
		self.label.pack(pady=0)

		# RGB =============================
		self.hexlab = tk.Label(self.root,
			text="RGB",
			font="Arial 20",
			)
		self.hexlab.pack(pady=0)
		self.rgb = tk.IntVar()
		self.label = tk.Entry(self.root,
			textvariable=self.rgb,
			font="Arial 20",
			)
		self.label.pack(pady=0)

	def rgb_to_hex(self, r, g, b):
		''' converts rgb to hex '''
		self.hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)


	def scalecommand2(self, scale_size):
		''' modify text in label = scale size '''
		self.color2 = int(scale_size)
		self.refresh_color()



	def scalecommand3(self, scale_size):
		''' modify text in label = scale size '''
		self.color3 = int(scale_size)
		self.refresh_color()


class ScaleColor:
	def __init__(self):
		self.var1 = tk.IntVar()
		self.scale = tk.Scale(app.root,
			variable=self.var1,
			from_=0, to=255, length=255,
			orient=tk.HORIZONTAL,
			command=self.scalecommand)
		self.scale.pack(pady=20)
		self.color = 0

	def scalecommand(self, scale_size):
		''' modify text in label = scale size '''
		self.color = int(scale_size)
		self.refresh_color()

	def refresh_color(self):
		''' each time the color changes it updates label and background '''
		app.rgb_to_hex(scale1.color, scale2.color, scale3.color)
		
		# app.label.config(textvariable=(app.hex))
		app.x.set(app.hex)
		app.rgb.set(f"{scale1.color},{scale2.color},{scale3.color}")
		app.root.config(background=app.hex)
		try:
			app.name.set(coldic[f"{scale1.color},{scale2.color},{scale3.color}"])
		except:
			app.name.set("UNKNOWN")
			# print(f"{scale1.color},{scale2.color},{scale3.color}")
			# # print(coldic[f"{scale1.color},{scale2.color},{scale3.color}"])
			# print(coldic["0,0,0"])


app = Window()
scale1 = ScaleColor()
scale2 = ScaleColor()
scale3 = ScaleColor()
app.loop()