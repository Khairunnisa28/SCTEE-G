import tkinter as tk

root = tk.Tk()
root.title("Odd Even Checker")

def check_number():
    number = int(entry.get())
    
    if number % 2 == 0:
        result.config(text="Even Number")
    else:
        result.config(text="Odd Number")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Check", command=check_number)
button.pack()

result = tk.Label(root, text="")
result.pack()

root.mainloop()
