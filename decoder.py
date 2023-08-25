import tkinter as tk
from tkinter import ttk

frame = tk.Tk()
frame.geometry("300x300")
frame.title("Decoder")
txt = tk.Text(frame, height=4, width=28)

def decoder(code, key):
    auth = all(item in code for item in key)
    if auth == True:
        global conv
        res = [ i for i in code if i not in key]
        conv = [chr(i) for i in res]
    else:
        label22.config(text="Wrong key")

TabControl = ttk.Notebook(frame)
Tab2 = ttk.Frame(TabControl)
TabControl.add(Tab2, text="Decoder")
TabControl.pack(expand=1, fil="both")

def TextIn ():
    In2 = TextField2.get()
    In3 = TextField3.get()
    decoder(code = list(map(int, In2.strip().split())), key = list(map(int, In3.strip().split())))
    label21.config(text = "".join(conv))

Text21 = ttk.Label(Tab2, text="Enter the code:")
Text21.pack(padx=5, pady=5)

TextField2 = ttk.Entry(Tab2,width=30)
TextField2.place(x=300, y=25)
TextField2.pack()

Text22 = ttk.Label(Tab2, text="Enter the key:")
Text22.pack(padx=5, pady=5)

TextField3 = ttk.Entry(Tab2,width=30)
TextField3.place(x=300, y=50)
TextField3.pack()

button23 = ttk.Button(Tab2, text="Convert", command=TextIn)
button23.place(x=350, y=75)
button23.pack(padx=5, pady=5)

label21 = ttk.Label(Tab2, text="")
label21.place(x=350, y=300)
label21.pack()

label22 = ttk.Label(Tab2, text="")
label22.place(x=350, y=300)
label22.pack()

frame.mainloop()