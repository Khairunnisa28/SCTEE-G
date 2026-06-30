import tkinter as tk

root = tk.Tk()
root.title("Simple App")

label = tk.Label(root, text="Hello Student!")
label.pack()

button = tk.Button(root, text="Click Me")
button.pack()

root.mainloop()