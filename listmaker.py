import tkinter as tk



def retrievedata():
    ''' get data stored '''
    global list_data
    list_data = []
    try:
      with open("save.txt", "r", encoding="utf-8") as file:
       for f in file:
        Frame2.listbox.insert(tk.END, f.strip())
        list_data.append(f.strip())
        print(list_data)
    except:
        pass

def reload_data():
    Frame2.listbox.delete(0, tk.END)
    for d in list_data:
        Frame2.listbox.insert(0, d)


def add_item(event=1):
    global list_data
    if Frame2.content.get() != "":
        Frame2.listbox.insert(tk.END, Frame2.content.get())
        list_data.append(Frame2.content.get())
        Frame2.content.set("")

def insert_item(event=1):

    global list_data
    if Frame2.content.get() != "":
        print(Frame2.listbox.curselection())
        pos = Frame2.listbox.curselection()[0] + 1
        Frame2.listbox.insert(pos, Frame2.content.get())
        if pos < len(list_data):
            list_data[pos] = Frame2.content.get()
        else:
            pass
        Frame2.content.set("")


def delete():
    global list_data
    Frame2.listbox.delete(0, tk.END)
    list_data = []


def delete_selected():

    try:
        selected = Frame2.listbox.get(Frame2.listbox.curselection())
        Frame2.listbox.delete(Frame2.listbox.curselection())
        list_data.pop(list_data.index(selected))
        Frame2.listbox.selection_set(0)
        print(Frame2.listbox.curselection())
    except:
        pass


def quit(destroy=1):
    if destroy:
        Window.root.destroy()
    else:
        with open("save.txt", "w", encoding="utf-8") as file:
            for d in list_data:
                file.write(d + "\n")

class Window:
    root = tk.Tk()
    root.title("List App")

class Frame1:
    frame1 = tk.Frame(Window.root)
    frame1.pack(side="left")

    # ADD ITEM
    button = tk.Button(frame1,
        text="Add Item",
        command=add_item)
    button.pack()

    button = tk.Button(frame1,
        text="Insert Item after",
        command=insert_item)
    button.pack()

    button_delete = tk.Button(frame1, text="Delete", command=delete)
    button_delete.pack()

    button_delete_selected = tk.Button(frame1, text="Delete Selected", command=delete_selected)
    button_delete_selected.pack()
    bquit = tk.Button(frame1, text="Save", command=lambda: quit(0))
    bquit.pack()

    bquit = tk.Button(frame1, text="Quit", command=quit)
    bquit.pack()

class Frame2:
    global list_data
    frame2 = tk.Frame(Window.root)
    frame2.pack(side="left", fill="both", expand=1)
    content = tk.StringVar()
    entry = tk.Entry(frame2, textvariable=content,
        bg="yellow")
    entry.pack(fill="both", expand=1)
    entry.focus()
    listbox = tk.Listbox(frame2)
    listbox.pack(fill="both", expand=1)
    entry.bind("<Return>", add_item)


retrievedata()
Window.root.mainloop()