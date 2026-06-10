import tkinter as tk

window = tk.Tk()
window.title("Stopwatch")
window.geometry("400x250")

running = False
seconds = 0


def update_time():
    global seconds

    if running:
        seconds += 1

        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60

        time_text = f"{hours:02}:{minutes:02}:{secs:02}"

        time_label.config(text=time_text)

        window.after(1000, update_time)


def start():
    global running

    if not running:
        running = True
        update_time()


def stop():
    global running
    running = False

def reset():
    global seconds, running

    running = False
    seconds = 0
    time_label.config(text="00:00:00")

time_label = tk.Label(
    window,
    text="00:00:00",
    font=("Helvetica", 32)
)
time_label.pack(pady=20)

button_frame = tk.Frame(window)
button_frame.pack()

start_button = tk.Button(
    button_frame,
    text="Start",
    command=start,
    width=10
)
start_button.grid(row=0, column=0, padx=5)

stop_button = tk.Button(
    button_frame,
    text="Stop",
    command=stop,
    width=10
)
stop_button.grid(row=0, column=1, padx=5)

reset_button = tk.Button(
    button_frame,
    text="Reset",
    command=reset,
    width=10
)
reset_button.grid(row=0, column=2, padx=5)

window.mainloop()