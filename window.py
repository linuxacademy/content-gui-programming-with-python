#!/usr/bin/env python
import tkinter as tk

root = tk.Tk()
root.geometry("500x300+200+200")
root.title("My Window")
root.iconphoto(True, tk.PhotoImage(file="icon.png"))

root.mainloop()
