import tkinter as tk
from tkinter import messagebox


def add_task():
    task = task_entry.get().strip()

    if task:
        active_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning(
            "Warning",
            "Please enter a task!"
        )


def delete_task():
    try:
        selected = active_listbox.curselection()[0]
        active_listbox.delete(selected)
    except IndexError:
        messagebox.showwarning(
            "Warning",
            "Please select a task to delete!"
        )


def mark_done():
    try:
        selected = active_listbox.curselection()[0]
        task = active_listbox.get(selected)

        active_listbox.delete(selected)
        completed_listbox.insert(tk.END, task)

    except IndexError:
        messagebox.showwarning(
            "Warning",
            "Please select a task to mark as done!"
        )


def clear_completed():
    if completed_listbox.size() == 0:
        messagebox.showinfo(
            "Info",
            "There are no completed tasks."
        )
        return

    answer = messagebox.askyesno(
        "Confirmation",
        "Are you sure you want to clear all completed tasks?"
    )

    if answer:
        completed_listbox.delete(0, tk.END)
        messagebox.showinfo(
            "Success",
            "Completed tasks cleared!"
        )


# ================= Window =================
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("500x650")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="To-Do List",
    font=("Helvetica", 18, "bold")
)
title_label.pack(pady=15)

# ================= Input =================
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

task_entry = tk.Entry(
    input_frame,
    width=30,
    font=("Helvetica", 12)
)
task_entry.grid(row=0, column=0, padx=5)

add_button = tk.Button(
    input_frame,
    text="Add Task",
    width=10,
    command=add_task
)
add_button.grid(row=0, column=1, padx=5)

# ================= Active Tasks =================
active_label = tk.Label(
    root,
    text="Active Tasks",
    font=("Helvetica", 12, "bold")
)
active_label.pack()

active_listbox = tk.Listbox(
    root,
    width=50,
    height=10,
    font=("Helvetica", 11)
)
active_listbox.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

delete_button = tk.Button(
    button_frame,
    text="Delete",
    width=12,
    command=delete_task
)
delete_button.grid(row=0, column=0, padx=5)

done_button = tk.Button(
    button_frame,
    text="Mark Done",
    width=12,
    command=mark_done
)
done_button.grid(row=0, column=1, padx=5)

# ================= Completed Tasks =================
completed_label = tk.Label(
    root,
    text="Completed Tasks",
    font=("Helvetica", 12, "bold")
)
completed_label.pack()

completed_listbox = tk.Listbox(
    root,
    width=50,
    height=10,
    font=("Helvetica", 11)
)
completed_listbox.pack(pady=5)

clear_button = tk.Button(
    root,
    text="Clear Completed",
    width=18,
    command=clear_completed
)
clear_button.pack(pady=15)

root.mainloop()