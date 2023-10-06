import tkinter as tk
from random import randint
from tkinter import PhotoImage
from PIL import Image
import os

# next features - 4.10.2023
# SAVE fav colors (button, save to text, append mode with data too)
# show in list all colors, when click on one show it in entry and on bg

# Writes the title in the colorsaved.html the first time only
empty=False
with open("colorsaved.html") as file:
    x = file.read()
    if x == "\n":
        empty = True

if empty:
    with open("colorsaved.html", "w") as file:
        file.write("<h1>Colorpicker by GiovanniPython</h1>\n<br><a href='https:\\pythonprogramming.altervista.org'>Visit my site, please</a>\n")


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

coldic = create_dic(get_csv("D:\\python\\apps\\colors.csv"))


# ====== TKINTER GUI ===========
class Window:

    def __init__(self):
        self.root = tk.Tk()
        self.hex="#000000"
        self.root.geometry("800x600")
        self.root.title("Colorpicker - pythonprogramming.altervista.org - YT GiovanniPython - X @pythonprogrammi")
        self.root.config(background="black")

    def scale(self):
        self.canvas = tk.Canvas(self.root, bg="black", width=800,
            height=100)
        self.canvas.config(highlightthickness=0, bg=self.hex)
        self.canvas.pack()
        self.img = PhotoImage(file="logo.png")
        self.canvas.create_image(0, 0, image=self.img, anchor="nw")
        self.red_scale = ScaleColor()
        self.green_scale = ScaleColor()
        self.blue_scale = ScaleColor()
        self.create_widgets()

    def loop(self):
        self.root.mainloop()


    def create_widgets(self):
        self.label_color_hex()
        self.color1 = 0
        self.color2 = 0
        self.color3 = 0


    def label_color_hex(self):
        self.frame0 = tk.Frame(self.root)
        self.frame0.pack(side="top")

        # NAME =========================
        self.frame1 = tk.Frame(self.frame0)
        self.frame1.pack(side="left")
        self.clrtext = tk.Label(self.frame1,
            text="Name",
            font="Arial 20",
            )
        self.clrtext.pack(pady=0)
        self.name = tk.StringVar()
        self.colorname = tk.Entry(self.frame1,
            textvariable=self.name,
            font="Arial 20",
            )
        self.colorname.pack(pady=0)

        # HEX ===========================
        self.frame2 = tk.Frame(self.frame0)
        self.frame2.pack(side="left")
        self.hexlab = tk.Label(self.frame2,
            text="Hexadecimal",
            font="Arial 20",
            )
        self.hexlab.pack(pady=0)
        self.x = tk.IntVar()
        self.label = tk.Entry(self.frame2,
            textvariable=self.x,
            font="Arial 20",
            )
        self.label.pack(pady=0)

        # RGB =============================
        self.frame3 = tk.Frame(self.frame0)
        self.frame3.pack(side="left")
        self.hexlab = tk.Label(self.frame3,
            text="RGB",
            font="Arial 20",
            )
        self.hexlab.pack(pady=0)
        self.rgb = tk.IntVar()
        self.label = tk.Entry(self.frame3,
            textvariable=self.rgb,
            font="Arial 20",
            )
        self.label.pack(pady=0)

        # BUTTON TO SAVE
        self.frame4 = tk.Frame(self.root)
        self.frame4.pack(side="left")
        self.savebut = tk.Button(
            self.frame4,
            text="Save color",
            command=self.savecolor
            )
        self.savebut.pack(side="left")

        self.openbut = tk.Button(
            self.frame4,
            text="Open saved colors",
            command=self.opensavedcolors
            )
        self.openbut.pack(side="left")

        self.openbut = tk.Button(
            self.frame4,
            text="Edit saved colors",
            command=self.editsavedcolors
            )
        self.openbut.pack(side="left")

    def savecolor(self):
        with open("colorsaved.html", "a") as file:
            file.write(f"<div style='background-color:{self.hex};color:{self.hex}'>..........................<i style='background-color:white'>{self.name.get()} {self.hex} {self.rgb_color}</i></div>\n")

    def opensavedcolors(self):
        os.system("colorsaved.html")

    def editsavedcolors(self):
        os.system("NOTEPAD.exe colorsaved.html")

    def rgb_to_hex(self, hx:tuple) -> str:
        ''' converts rgb to hex '''
        self.rgb_color = r,g,b = hx
        self.hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        return self.hex


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
        self.frame = tk.Frame(app.root)
        self.frame.pack(padx=(0, 0), pady=(10, 0))
        self.color = 0
        self.var1 = tk.IntVar()
        self.scale = tk.Scale(self.frame,
            variable=self.var1,
            from_=0, to=255, length=255,
            orient=tk.HORIZONTAL,
            command=self.scalecommand)
        self.scale.pack(side="left")

    def scalecommand(self, scale_size):
        ''' modify text in label = scale size '''
        self.color = int(scale_size)
        self.refresh_color()

    def refresh_color(self):
        ''' each time the color changes it updates label and background '''
        rgb = app.red_scale.color,app.green_scale.color,app.blue_scale.color
        print(rgb)
        hexadecimal = app.rgb_to_hex(rgb)
        rgb = "{},{},{}".format(*rgb)
        print(rgb)
        # app.label.config(textvariable=(app.hex))
        app.x.set(hexadecimal)
        app.rgb.set(rgb)
        app.root.config(background=hexadecimal)
        app.canvas.config(bg=hexadecimal)
        try:
            app.name.set(coldic[rgb])
        except:
            app.name.set("?")


app = Window()
app.scale()
app.loop()