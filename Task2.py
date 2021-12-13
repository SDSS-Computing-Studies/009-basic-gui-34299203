#! python3
import tkinter as tk
from tkinter import *
from tkinter import ttk
window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")
dogphoto = PhotoImage(file="dog.png")
entry1 = tk.Entry(window, width = 20)
entry2 = tk.Entry(window, width = 20)
entry3 = tk.Entry(window, width = 20)
entry4 = tk.Entry(window, width = 20)
entry5 = tk.Entry(window, width = 20)
Label2 = tk.Label("Name")
Label2 = tk.Label("Type")
Label2 = tk.Label("Breed")
Label2 = tk.Label("Owner")
Label2 = tk.Label("Birthdate")