import tkinter as tk
from tkinter import ttk
import pyperclip

# # # # # # 
frame = tk.Tk()
frame.geometry("300x300")
frame.title("pydotCODE")
txt = tk.Text(frame, height=4, width=28)
# # # # # # 

# Converting characters into ASCII
def encoder(string):
    global asc
    split = [*string]
    asc = [ord(i) for i in split] 
    
# Converting ASCII back into characters
def decoder(code):
    global conv
    conv = [chr(i) for i in code]

# # # # # # 
TabControl = ttk.Notebook(frame)
Tab1 = ttk.Frame(TabControl)
Tab2 = ttk.Frame(TabControl)
TabControl.add(Tab1, text="Coder")
TabControl.add(Tab2, text="Decoder")
TabControl.pack(expand=1, fil="both")
# # # # # # 

# # # # # # 
def TextIn ():
    Encode = encodeField.get()
    Decode = decodeField.get()
    encoder(string = Encode)
    decoder(code = list(map(int, Decode.strip().split())))
    codeOut.config(text = " ".join(map(str, asc)))
    msgOut.config(text = "".join(conv))
# # # # # # 

# # # # # # 
def copyFn():
    copyCode = pyperclip.copy(" ".join(map(str, asc)))
# # # # # # 


# Encoder
labelEn = ttk.Label(Tab1, text="Enter the message:")
labelEn.pack()

encodeField = ttk.Entry(Tab1, width=30)
encodeField.place(x=350, y=250)
encodeField.pack(padx=5, pady=5)

convertbtn = ttk.Button(Tab1, text  ="Convert", command = TextIn)
convertbtn.place(x=350, y=300)
convertbtn.pack(padx=10, pady=5)

codeOut = ttk.Label(Tab1, text="")
codeOut.place(x=350, y=300)
codeOut.pack()

copybtn = ttk.Button(Tab1, text="Copy code", command=copyFn)
copybtn.place(x=350, y=300)
copybtn.pack(padx=10, pady=5)
# # # # # # 

# Decoder
labelDe = ttk.Label(Tab2, text="Enter the code:")
labelDe.pack(padx=5, pady=5)

decodeField = ttk.Entry(Tab2,width=30)
decodeField.place(x=300, y=25)
decodeField.pack()

convertbtn2 = ttk.Button(Tab2, text="Convert", command=TextIn)
convertbtn2.place(x=350, y=75)
convertbtn2.pack(padx=5, pady=5)

msgOut = ttk.Label(Tab2, text="")
msgOut.place(x=350, y=300)
msgOut.pack()
# # # # # # 

frame.mainloop()