import tkinter as tk
from tkinter import messagebox
from database import Database

db = Database()

def open_withdraw_window(student):
    win = tk.Toplevel()
    win.title("Withdraw Subject")
    win.geometry("300x150")

    tk.Label(win, text="Enter subject to remove:").pack()
    subject_entry = tk.Entry(win)
    subject_entry.pack()

    def remove():
        name = subject_entry.get()
        for sub in student.subjects:
            if sub.id == name:
                student.subjects.remove(sub)
                # Update the student info in the database
                db.update_student(student)
                # Show message when subject is withdrawn
                messagebox.showinfo("Removed", f"{name} has been removed.")
                win.destroy()
                return
                # Show error if subject not found
        messagebox.showerror("Not Found", f"No subject named {name}.")
        # Button to remove the subject
    tk.Button(win, text="Remove", command=remove).pack(pady=10)
