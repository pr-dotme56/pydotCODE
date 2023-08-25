import datetime
import tkinter as tk
from tkinter import ttk
import pyperclip

frame = tk.Tk()
frame.geometry("300x250")
frame.title("Coder")
txt = tk.Text(frame, height=4, width=28)

def coder(string):
    global asc
    global key
    date = datetime.datetime.now()
    hours, minutes, seconds = date.hour, date.minute, date.second
    split = [*string]
    asc = [ord(i) for i in split] 
    asc.extend([hours, minutes, seconds])
    key = [hours, minutes, seconds]

TabControl = ttk.Notebook(frame)
Tab1 = ttk.Frame(TabControl)
TabControl.add(Tab1, text="Coder")
TabControl.pack(expand=1, fil="both")

def TextIn ():
    In1 = TextField1.get()
    coder(string = In1)

def out11():
    ccode = pyperclip.copy(" ".join(map(str, asc)))
    label11.config(text = " ".join(map(str, asc)))

def out12():
    ckey = pyperclip.copy("".join(map(str, key)))
    label12.config(text=" ".join(map(str, key)))

Text11 = ttk.Label(Tab1, text="Enter the message:")
Text11.pack()

TextField1 = ttk.Entry(Tab1, width=30)
TextField1.place(x=350, y=250)
TextField1.pack(padx=5, pady=5)

button11 = ttk.Button(Tab1, text  ="Convert", command = TextIn)
button11.place(x=350, y=300)
button11.pack(padx=10, pady=5)

button12 = ttk.Button(Tab1, text="Copy code", command=out11)
button12.place(x=350, y=300)
button12.pack(padx=10, pady=5)

label11 = ttk.Label(Tab1, text="")
label11.place(x=350, y=300)
label11.pack()

button13 = ttk.Button(Tab1, text="Copy key", command=out12)
button13.place(x=350, y=300)
button13.pack(padx=10, pady=5)

label12 = tk.Label(Tab1, text="")
label12.place(x=350, y=300)
label12.pack()

frame.mainloop()