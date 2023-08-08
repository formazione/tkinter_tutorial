# D:\github\tkinter_tutorial\filebrowser.py

# filebrowser.py
#show the content of the file in the listbox on the left into the text area on the right when seltect one item

from glob import glob
import tkinter as tk

class Show:
    def __init__(self):
        self.files = glob("*.py")

    def __call__(self):
        self.window()

    def window(self):
        self.root = tk.Tk()
        self.showfilestk()
        self.root.mainloop()

    def showfilestk(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.list_tk = tk.Listbox(self.frame)
        self.list_tk.pack(
            side="left", anchor="n", fill="both")
        # self.list_tk.bind("<Button>", self.show_doc)
        self.list_tk.bind("<<ListboxSelect>>", self.show_doc)
        # self.list_tk.bind("<ButtonRelease-1>", self.get_selected_item)
        self.text = tk.Text(self.frame)
        self.text.pack(side="left")
        for f in self.files:
            self.list_tk.insert(tk.END, f)
            self.list_tk.pack()
    
    def intext(self, text):
        ''' insert the name of the text passed as argument '''
        self.text.insert(tk.END, text)

    def text_delete(self):
        ''' delete everything in text widget '''
        self.text.delete("0.0", tk.END)

    def intext_filecontent(self, filename):
        ''' open file name (item selected) and shows content '''
        with open(filename) as file:
            self.intext(file.read())

    def show_doc(self, event=' '):
        ''' get the item name and stores it in selected_item to show info about it (file.py)'''
        selected_indices = self.list_tk.curselection()
        selected_index = selected_indices[0]
        selected_item = self.list_tk.get(selected_index)
        print("Selected item:", selected_item)
        self.text_delete()
        self.intext_filecontent(selected_item)
        # with open(selected_item) as file:






show = Show()
show()

"""
# Example to get items

import tkinter as tk

class MyApplication:
    def __init__(self, root):
        self.root = root

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.list_tk = tk.Listbox(self.frame)
        self.list_tk.pack(side="left", anchor="n")

        self.list_tk.insert("end", "Item 1")
        self.list_tk.insert("end", "Item 2")
        self.list_tk.insert("end", "Item 3")

        self.get_selected_button = tk.Button(self.frame, text="Get Selected", command=self.get_selected_item)
        self.get_selected_button.pack()

    def get_selected_item(self):
        selected_indices = self.list_tk.curselection()
        if selected_indices:
            selected_index = selected_indices[0]
            selected_item = self.list_tk.get(selected_index)
            print("Selected item:", selected_item)

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApplication(root)
    root.mainloop()




"""