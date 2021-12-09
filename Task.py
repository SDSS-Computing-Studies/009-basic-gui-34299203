#!python3
import tkinter as tk
from tkinter import *
from tkinter import ttk
window = tk.Tk()
window.title("tk")
entry1 = tk.Entry(window, width = 30)
Label2 = tk.Label(text ="x")
entry2 = tk.Entry(window, width = 30)
Label3 = tk.Label(text ="=")
entry3 = tk.Entry(window, width = 30)
window.geometry("450x25")
entry1.pack(side=LEFT)
Label2.pack(side=LEFT)
entry2.pack(side=LEFT)
Label3.pack(side=LEFT)
entry3.pack(side=LEFT)
window.mainloop()
