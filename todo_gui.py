import tkinter as tk
from tkinter import messagebox
from todo_class import ToDo

class GUi:
    def __init__(self):
        self.todo = ToDo()
        self.start = False

        if self.start:
            self.root = tk.Tk()
            self.root.title('button')
            self.root.geometry('300x400')

    def button_command(self, cmd):
        self.button = tk.Button(root, command=cmd)
        self.button.pack(padx=10, pady=10)


    def new_screen(self):
        self.root.withdraw()
        self.new = tk.Toplevel(self.root)
        self.new.title('new')
        self.new.geometry('300x300')
        
    def main(self):
        if self.todo.add_called == True:
            self.button_command(self.new_screen)

        self.root.mainloop()