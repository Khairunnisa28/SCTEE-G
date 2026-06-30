import tkinter as tk

window = tk.Tk()
window.title("Kalkulator")
window.geometry("360x550")
window.resizable(False, False)

# =========================
# MODE
# =========================
dark_mode = True

# WARNA DARK MODE
bg_dark = "#1e1e1e"
fg_dark = "white"
button_dark = "#333333"
operator_dark = "#444444"

# WARNA LIGHT MODE
bg_light = "white"
fg_light = "black"
button_light = "#dddddd"
operator_light = "#cccccc"

# =========================
# DATA
# =========================
expression = ""

# =========================
# FUNCTION
# =========================
def tekan(nilai):
    global expression
    expression += str(nilai)
    hasil.config(text=expression)

def clear():
    global expression
    expression = ""
    hasil.config(text="0")

def backspace():
    global expression
    expression = expression[:-1]
    if expression == "":
        hasil.config(text="0")
    else:
        hasil.config(text=expression)

def hitung():
    global expression
    try:
        expression = str(eval(expression))
        hasil.config(text=expression)
    except:
        hasil.config(text="Error")
        expression = ""

def ubah_mode():
    global dark_mode
    dark_mode = not dark_mode

    if dark_mode:
        window.config(bg=bg_dark)
        hasil.config(bg=bg_dark, fg=fg_dark)

        for tombol in semua_tombol:
            if tombol["text"] in ["÷", "×", "-", "+", "="]:
                tombol.config(bg=operator_dark, fg=fg_dark)
            else:
                tombol.config(bg=button_dark, fg=fg_dark)

        tombol_mode.config(bg=button_dark, fg=fg_dark)

    else:
        window.config(bg=bg_light)
        hasil.config(bg=bg_light, fg=fg_light)

        for tombol in semua_tombol:
            if tombol["text"] in ["÷", "×", "-", "+", "="]:
                tombol.config(bg=operator_light, fg=fg_light)
            else:
                tombol.config(bg=button_light, fg=fg_light)

        tombol_mode.config(bg=button_light, fg=fg_light)

# =========================
# DISPLAY
# =========================
hasil = tk.Label(
    window,
    text="0",
    font=("Arial", 30),
    anchor="e",
    padx=20
)
hasil.pack(fill="x", pady=20)

# =========================
# BUTTON FRAME
# =========================
frame = tk.Frame(window)
frame.pack()

semua_tombol = []

data_tombol = [
    ("C", clear),
    ("⌫", backspace),
    ("÷", lambda: tekan("/")),
    ("×", lambda: tekan("*")),

    ("7", lambda: tekan("7")),
    ("8", lambda: tekan("8")),
    ("9", lambda: tekan("9")),
    ("-", lambda: tekan("-")),

    ("4", lambda: tekan("4")),
    ("5", lambda: tekan("5")),
    ("6", lambda: tekan("6")),
    ("+", lambda: tekan("+")),

    ("1", lambda: tekan("1")),
    ("2", lambda: tekan("2")),
    ("3", lambda: tekan("3")),
    ("=", hitung),

    ("0", lambda: tekan("0")),
    (".", lambda: tekan(".")),
]

row = 0
col = 0

for text, cmd in data_tombol:
    tombol = tk.Button(
        frame,
        text=text,
        width=7,
        height=3,
        font=("Arial", 14),
        command=cmd,
        bd=0
    )
    tombol.grid(row=row, column=col, padx=4, pady=4)
    semua_tombol.append(tombol)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Tombol Dark Mode
tombol_mode = tk.Button(
    window,
    text="Dark / Light Mode",
    font=("Arial", 12),
    command=ubah_mode,
    bd=0
)
tombol_mode.pack(pady=15)

# Mode awal
ubah_mode()

window.mainloop()