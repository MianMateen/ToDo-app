import tkinter as tk
root = tk.Tk()
root.geometry('300x300')
root.title('Time')
root_label = tk.Label(root, text='Time: 0', font=('Times New Roman', 16))
root_label.pack(padx=10, pady=10)

root.mainloop()