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
