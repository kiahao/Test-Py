import tkinter as tk                      

root = tk.Tk()                           
root.title("Ví dụ")                       
root.geometry("300x150")
def chao():                               
    lbl.config(text="Xin chào!")

lbl = tk.Label(root, text="...")          
lbl.pack(pady=10)                         
tk.Button(root, text="Bấm", command=chao).pack()  

root.mainloop()                         