import time
import tkinter as tk
from tkinter import messagebox

class Wpm:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('600x600')
        self.root.title('Time')
        self.root_label = tk.Label(self.root, text='Time: 0', font=('Times New Roman', 16))
        self.root_label.pack(padx=10, pady=10)
        self.root_textbox = tk.Text(self.root, height=10, width=30)
        self.root_textbox.pack(padx=40, pady=40)
        self.start_time = time.perf_counter()

    
    def elapsed_time(self):
        self.current_time = time.perf_counter()
        self.elapsed = self.current_time - self.start_time
        self.elapsed_in_minutes = self.elapsed / 60
        self.characters = self.root_textbox.get('1.0', 'end-1c')
        self.words = len(self.characters) / 5
        self.wpm = self.words / self.elapsed_in_minutes
        self.root_label.config(text=f'Time: {self.elapsed:.2f}')
        self.root.after(100, self.elapsed_time)
        
        if self.elapsed > 30:
            self.root.destroy()
            messagebox.showinfo(title='WPM Result', message=f'wpm = {self.wpm:.2f}')
                
wpm = Wpm()
    

if __name__ == '__main__':
    wpm.elapsed_time()
    wpm.root.mainloop()
