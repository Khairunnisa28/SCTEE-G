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